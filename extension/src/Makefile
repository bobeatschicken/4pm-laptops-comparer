CXX=dogescript
CXXFLAGS=--beautify

JSFILES=background.js \
		konami/inject_richert.js \
		popup/index.js \
		popup/select.js \
		jwt/inject_jwt.js \
		jwt/jwt.js

all: ${JSFILES}

background.js: background.djs
	${CXX} $^ ${CXXFLAGS} > $@

konami/inject_richert.js: konami/inject_richert.djs
	${CXX} $^ ${CXXFLAGS} > $@

jwt/inject_jwt.js: jwt/inject_jwt.djs
	${CXX} $^ ${CXXFLAGS} > $@

jwt/jwt.js: jwt/jwt.djs
	${CXX} $^ ${CXXFLAGS} > $@

popup/index.js: popup/index.djs
	${CXX} $^ ${CXXFLAGS} > $@

popup/select.js: popup/select.djs
	${CXX} $^ ${CXXFLAGS} > $@

clean:
	rm -f ${JSFILES}

.PHONY: all clean
