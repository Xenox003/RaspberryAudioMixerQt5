git pull origin

for file in ./.compileui/*.ui; do
    pureFileName=${file##*/}

    echo $PWD
    pyuic5 "$file" -o "app/modules/ui/compiled/ui_${pureFileName//.ui/}.py"
done

git add *
git commit -a -m "Auto: UI Update"