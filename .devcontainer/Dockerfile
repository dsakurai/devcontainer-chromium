FROM debian:stable-slim

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
	# Chromium
	chromium fonts-noto-cjk \
	# Development
	sudo ca-certificates curl python3 git ssh neovim \
	&& rm -rf /var/lib/apt/lists/*

RUN groupadd --gid ${USER_GID} ${USERNAME} \
	&& useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
	&& echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} \
	&& chmod 0440 /etc/sudoers.d/${USERNAME}

RUN mkdir -p /workspaces && chown ${USERNAME}:${USER_GID} /workspaces
WORKDIR /workspaces

USER ${USERNAME}

ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# RUN uv python install 3.13
