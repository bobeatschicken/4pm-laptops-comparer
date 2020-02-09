CXX=dogescript
CXXFLAGS=--beautify

JSFILES=background.js \
		inject_richert.js \
		popup/index.js

all: ${JSFILES}

background.js: background.djs
	${CXX} $^ ${CXXFLAGS} > $@

inject_richert.js: inject_richert.djs
	${CXX} $^ ${CXXFLAGS} > $@

popup/index.js: popup/index.djs
	${CXX} $^ ${CXXFLAGS} > $@

clean:
	rm -f ${JSFILES}

.PHONY: all clean
