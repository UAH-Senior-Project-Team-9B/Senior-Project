FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Update the image to the latest packages
RUN apt-get update \
    && apt-get upgrade --yes \
    # Install Node.js and NPM
    # https://github.com/nodesource/distributions/blob/master/README.md
    && curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install --yes --no-install-recommends nodejs=22.12.0* \
    && rm -rf /var/lib/apt/lists/* \
    && echo "alias task='uv run task'" >> /etc/bash.bashrc

USER vscode
ENV PATH="/home/vscode/.local/bin:${PATH}"

# Install UV
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
