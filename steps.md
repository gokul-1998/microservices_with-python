


- after installing docker if `kubectl` did'nt work
    - `sudo usermod -aG docker $USER && newgrp docker`

- We need to install k9s
    - `https://github.com/derailed/k9s`
    - `snap install k9s --devmode`

- to build a docker image, create a  docker file and  in  the same directory use 
    - `docker build .`

- `docker  tag c5ba91214195dcf28d40 gokulkris/auth:latest`
    - this is how we tag a container

- use `docker login` to login to docker hub

- in minikube press `0` to view all kube containers

- go into manidest directory and type
    - `kubectl apply -f ./`
- press `esc` to  come out  of  a container
- press `s` to access the container shell of  container
- `env` is  the command to get  the environment variables
- `env | grep MYSQL` 
    - to see all the env variables 

- type `exit` in tht shell to exit out  of it

- we dont need to create a repo in docker hub, it will automatically create the  repo for us in docker hub as soon as we push if  the repo doesnt exist