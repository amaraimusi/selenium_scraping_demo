#!/bin/sh
echo 'ソースコードを差分アップロードします。'

rsync -auvz ../ amaraimusi@amaraimusi.sakura.ne.jp:www/selenium_scraping_demo/

echo "------------ Success"
#cmd /k