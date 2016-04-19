# maven picker
===

## why picker
===

当你准备吧一堆java(maven)的git项目打包带走时, 发现有这样的情况:

```
du -h my_code_dir

...
...
 24K    ../xiaochao-svr/flash-web/src/main/resources/spring
 40K    ../xiaochao-svr/flash-web/src/main/resources
8.0K    ../xiaochao-svr/flash-web/src/main/webapp/WEB-INF
8.0K    ../xiaochao-svr/flash-web/src/main/webapp
 92K    ../xiaochao-svr/flash-web/src/main
 92K    ../xiaochao-svr/flash-web/src
100K    ../xiaochao-svr/flash-web

2.31G my_code_dir
```
你需要把maven产出target全部干掉, 只留下干净的代码, 然后让你快速的打成tar包带走.

## GET START
```
git clone git@github.com:LuoDi-Nate/mavenPicker.git

cd maven_picker

python mavenCleaner.py $your_code_path
```
picker会递归把你$your_code_path下的所有maven项目找到, 并执行
'mvn clean'

## ENJOY IT!
```
^_^
```
