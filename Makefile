
.PHONY: tests serve clean quality


SOURCEDIR = "cookingchrono/"

CONTAINER_RUNNER=podman

# If the first argument is "tests"...
ifeq (tests,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "tests"
  TESTS_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(TESTS_ARGS):dummy;@:)
endif


tests: build-devbox # Execution des tests
	$(call execute_cmd) run pytest -c pyproject.toml -s --log-cli-level=10 -o junit_family=xunit2 --junitxml=./junit_report.xml --cov-report xml:cov.xml --cov-report html --cov=${SOURCEDIR} --color=yes $(TESTS_ARGS)


quality: build-devbox # Execution des outils de qualité
	$(call execute_cmd) run black -l 200 --config pyproject.toml --target-version py38 /opt/${SOURCEDIR}
	$(call execute_cmd) run isort ${SOURCEDIR}
	$(call execute_cmd) run flake8 ${SOURCEDIR} --ignore=E501


run:
	python3 ./coockingchrono/main.py


clean: # Ménage des fichiers générés
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	rm -f junit_report.xml
	rm -Rf .coverage
	rm -Rf dist
	rm -Rf *.egg-info
	rm -Rf .pytest_cache

# If the first argument is "poetry"...
ifeq (poetry,$(firstword $(MAKECMDGOALS)))
  # use the rest as arguments for "poetry"
  POETRY_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(POETRY_ARGS):dummy;@:)
endif

poetry: build-devbox
	$(call execute_cmd) $(POETRY_ARGS)

build-devbox: # Construction de l'image de dev
	$(CONTAINER_RUNNER) build -t cookingchrono-devbox -f Dockerfile.dev .

define execute_cmd
	$(CONTAINER_RUNNER) run -i -v ${CURDIR}:/opt/cookingchrono cookingchrono-devbox $(1)
endef

build-buildozer: # Construction de l'image de dev
	podman build -t cookingchrono-buildozer -f Dockerfile .

deploy:
	podman run -it \
					--privileged \
					--volume /dev/bus/usb:/dev/bus/usb \
					--volume buildozer_home:/root/.buildozer \
					--volume ~/.android:/root/.android \
					--volume ${CURDIR}:/home/user/hostcwd \
					cookingchrono-buildozer android debug deploy run logcat
