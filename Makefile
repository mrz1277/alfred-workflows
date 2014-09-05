all: clean 4shared naver.movie torrent

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

torrent:
	cd net.yakiyama.alfred.torrent ; \
	zip ../workflows/torrent.alfredworkflow . -r --exclude=*.DS_Store* --exclude=*.pyc*
	cd ../ ; \