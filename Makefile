all: clean 4shared naver.movie

clean:
	rm -f workflows/*.alfredworkflow

4shared:
	cd net.yakiyama.alfred.4shared ; \
	zip ../workflows/4shared.alfredworkflow . -r --exclude=*.DS_Store* --exclude=*.pyc*
	cd ../ ; \

naver.movie:
	cd net.yakiyama.alfred.naver.movie ; \
	zip ../workflows/naver.movie.alfredworkflow . -r --exclude=*.DS_Store* --exclude=*.pyc*
	cd ../ ; \