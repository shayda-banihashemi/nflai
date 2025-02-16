FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y \
  zsh \
  curl \
  build-essential \
  wget \
  libreadline-dev \
  zlib1g-dev \
  libsqlite3-dev \
  unzip \
  libssl-dev \
  libffi-dev

SHELL ["/bin/zsh", "-c", "-o", "pipefail"]
RUN cd /tmp \
    && wget https://www.sqlite.org/2021/sqlite-autoconf-3350000.tar.gz \
    && tar -xvzf sqlite-autoconf-3350000.tar.gz \
    && cd sqlite-autoconf-3350000 \
    && ./configure --prefix=/usr \
    && make \
    && make install \
    && cd .. \
    && wget https://www.python.org/ftp/python/3.12.8/Python-3.12.8.tgz \
    && tar -xvzf Python-3.12.8.tgz \
    && cd Python-3.12.8 \
    && ./configure --enable-optimizations \
    && make \
    && make altinstall \
    && rm -rf /tmp/*

RUN if ! getent passwd app; then groupadd -g 1000 app \
    && useradd -u 1000 -g 1000 -d /home/app -m -s /bin/zsh app; fi \
    && echo app:app | chpasswd \
    && echo 'app ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && mkdir -p /etc/sudoers.d \
    && echo 'app ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/app \
    && chmod 0440 /etc/sudoers.d/app \
    && apt-get autoremove \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

USER app
WORKDIR /home/app

RUN touch /home/app/.zshrc \
   && echo 'PS1="$ "' >> /home/app/.zshrc \
   && echo 'export PATH=/home/app/.local/bin:/usr/local/bin:$PATH' >> /home/app/.zshrc


ENV PATH="/home/app/local/bin:/home/app/.local/bin:/usr/local/bin:${PATH}"
RUN curl -sSL https://install.python-poetry.org | python3.12 - \
    && poetry new app --src \
    && mkdir -p /home/app/data

ENV COLORTERM=truecolor
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /home/app/app
EXPOSE 5000
RUN export CURRENT_USER=$(whoami) && export CURRENT_GROUP=$(id -gn ${CURRENT_USER})
COPY --chown=${CURRENT_USER} pyproject.toml .
COPY --chown=${CURRENT_USER} src /home/app/app/src/
COPY --chown=${CURRENT_USER} tests /home/app/app/tests/
COPY --chown=${CURRENT_USER} data data/
RUN /home/app/.local/bin/poetry install

CMD ["poetry", "run", "python", "src/nflai/app.py"]
