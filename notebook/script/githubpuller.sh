
echo "Hello world"

mkdir -p /tmp/assignments
git clone "https://github.com/limbuu/course2.git" /tmp/assignments
echo "clone successful"

mkdir -p /home/jovyan/work/course101/source
mkdir -p /home/jovyan/work/course101/release
cp -rf /tmp/assignments/work/course101/source/. /home/jovyan/work/course101/source
cp -rf /tmp/assignments/work/course101/release/. /home/jovyan/work/course101/release

echo "copy successful"

mkdir -p /home/jovyan/work/course101/autograded
echo "autograded directory made"