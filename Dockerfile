FROM python:3.12-slim-bullseye
RUN apt-get update && apt-get install -y zsh curl
SHELL ["/bin/zsh", "-c", "-o", "pipefail"]

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
   && echo 'export PATH=/home/app/.local/bin:$PATH' >> /home/app/.zshrc

RUN \
    source /home/app/.zshrc \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry new app --src \
    && mkdir -p /home/app/data

ENV PATH="/home/app/local/bin:${PATH}"
ENV COLORTERM=truecolor
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /home/app/app
COPY --chown=shaydabanihashemi pyproject.toml .
RUN /home/app/.local/bin/poetry shell && /home/app/.local/bin/poetry install
COPY --chown=shaydabanihashemi src/ /home/app/app/app
COPY --chown=shaydabanihashemi tests/ /home/app/app/tests/

CMD ["python"]

