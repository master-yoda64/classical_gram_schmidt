# syntax = docker/dockerfile:1
FROM ubuntu:24.04
SHELL ["/bin/bash", "-c"]

# apt-get
RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.iij.ad.jp/pub/linux/ubuntu/archive/%g" /etc/apt/sources.list
#タイムゾーン
ENV TZ=Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata

# apt-get更新 wget取得
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
    wget \
    apt-utils \
    curl \
    nano \
    software-properties-common \
    build-essential \
    git \
    g++ \
    gcc \
    make \
    cmake \
    gfortran \
    pkg-config \
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

#===================================#
# ssh setup                         #
#===================================#
WORKDIR /root
RUN apt update && apt install openssh-client openssh-server -y
RUN --mount=type=secret,id=ssh_key,dst=/root/.ssh/id_rsa \
    mkdir -p /root/.ssh && \
    ssh-keyscan github.com >> /root/.ssh/known_hosts

#===================================#
# python and pip installation       #
#===================================#

ENV PYTHONIOENCODING "utf-8"
RUN apt-get install -y python3-pip python3-dev python3-setuptools

#===================================#
# rust installation                 #
#===================================#
ENV RUST_HOME /usr/local/lib/rust
ENV RUSTUP_HOME ${RUST_HOME}/rustup
ENV CARGO_HOME ${RUST_HOME}/cargo
RUN mkdir /usr/local/lib/rust && \
    chmod 0755 $RUST_HOME
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > ${RUST_HOME}/rustup.sh \
    && chmod +x ${RUST_HOME}/rustup.sh \
    && ${RUST_HOME}/rustup.sh -y --default-toolchain nightly --no-modify-path
ENV PATH $PATH:$CARGO_HOME/bin

RUN apt install libssl-dev
WORKDIR /root
