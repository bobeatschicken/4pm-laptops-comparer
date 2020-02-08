CXX=dogescript

all: background.js popup/index.js

background.js: background.djs
	${CXX} $^ --beautify > $@

popup/index.js: popup/index.djs
	${CXX} $^ --beautify > $@

clean:
	rm -f background.js popup/index.js

.PHONY: all clean
