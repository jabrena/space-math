FROM gitpod/workspace-full

# Install custom tools, runtimes, etc.
# For example "bastet", a command-line tetris clone:
# RUN brew install bastet
#
# More information: https://www.gitpod.io/docs/config-docker/

# Install Graphviz
RUN sudo apt-get update

# Install Java 17
RUN bash -c ". /home/gitpod/.sdkman/bin/sdkman-init.sh && sdk install java 17.0.0-tem"

# Install jbang
RUN bash -c ". /home/gitpod/.sdkman/bin/sdkman-init.sh && sdk install jbang"