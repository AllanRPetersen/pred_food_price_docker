# Data analysis
- Document here the project: pred_food_price_docker
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for pred_food_price_docker in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/pred_food_price_docker`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "pred_food_price_docker"
git remote add origin git@github.com:{group}/pred_food_price_docker.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
pred_food_price_docker-run
```

# Install

Go to `https://github.com/{group}/pred_food_price_docker` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/pred_food_price_docker.git
cd pred_food_price_docker
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
pred_food_price_docker-run
```
