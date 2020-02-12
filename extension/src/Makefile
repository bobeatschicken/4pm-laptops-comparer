CXX=dogescript
CXXFLAGS=--beautify

JSFILES=background.js \
		konami/inject_richert.js \
		popup/index.js

all: ${JSFILES}

background.js: background.djs
	${CXX} $^ ${CXXFLAGS} > $@

konami/inject_richert.js: konami/inject_richert.djs
	${CXX} $^ ${CXXFLAGS} > $@

popup/index.js: popup/index.djs
	${CXX} $^ ${CXXFLAGS} > $@

clean:
	rm -f ${JSFILES}

.PHONY: all clean