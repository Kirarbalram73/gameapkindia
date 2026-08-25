pkg install jadx
pkg install apktool
cd /sdcard/Download
apktool d app_name.apk
apktool d y1com.apk
jadx-gui y1com.apk
cd /sdcard/Download/y1com.apk/smali
grep -r "onTouch" .
grep -r "reset" .
grep -r "column" .
grep -r "history" .
grep -r "percent" .
find . -name "*Game*.smali" -o -name "*Activity*.smali" -o -name "*Board*.smali" -o -name "*Bet*.smali"
head -50 ./y1com/smali/com/cocos/game/AppCcActivity.smali
head -50 ./y1com/smali/com/google/androidgamesdk/GameActivity.smali
cd /sdcard/Download/y1com.apk/assets
ls -la | grep -E "\.js$|\.lua$|\.json$"
find . -name "*.js" -o -name "*.lua" | head -20
grep -n "column\|cow\|history\|percent\|tap\|reset\|index" ./y1com/assets/main.js | head -30
grep -n "column\|cow\|history\|percent\|tap\|reset\|index" ./y1com/assets/src/chunks/bundle.js | head -30
grep -n "column\|cow\|history\|percent\|tap\|reset\|index" ./y1com/assets/src/application.js | head -30
grep -rn "cc.Class\|cc.Component" ./y1com/assets/src/ --include="*.js" | head -20
grep -n "column\|cow\|history\|percent\|tap\|reset\|index" ./y1com/assets/main.js | head -30
grep -n "column\|cow\|history\|percent\|tap\|reset\|index" ./y1com/assets/src/chunks/bundle.js | head -30
grep -n "column\|cow\|history\|percent\|tap\|reset\|index" ./y1com/assets/src/application.js | head -30
grep -n "cow" ./y1com/assets/main.js
grep -n "13" ./y1com/assets/main.js | grep -i column
