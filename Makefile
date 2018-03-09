SOURCE_PATH = src
SOURCE_FILES = $(shell find $(SOURCE_PATH) -type f -name '*.py')
BUILD_PATH = tests/wrapped
BUILD_FILES = $(subst $(SOURCE_PATH),$(BUILD_PATH),$(SOURCE_FILES))

all: build

build: $(BUILD_FILES)

clean:
	rm -rf $(BUILD_FILES)
	rm -rf $(shell find . -type f -name *.pyc)

test: build
	python -m unittest tests

$(BUILD_PATH)/%.py: $(SOURCE_PATH)/%.py
	echo "def run():" > $@
	sed -e 's/^/    /' $? >> $@
