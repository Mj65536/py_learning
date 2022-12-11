import os
import zipfile
import shutil
import time

pd = {
    "p0": r"C:\Users\Hddlex\AppData\Roaming\.minecraft\saves",
    "p1": r"C:\Users\Hddlex\AppData\Roaming\.minecraft\saves\IndustrialCraft",
    "p2": r"F:\game\Minecraft\Minecraft\Java_1.12.2",
    "p3": r"F:\game\Minecraft\Minecraft\Java_1.12.2\IndustrialCraft.zip",
    "p4": r"F:\game\Minecraft\Minecraft\Java_1.12.2\IndustrialCraftOLD.zip",
    "p5": r"D:\tmp\IndustrialCraft.zip",
    "p6": r"F:\game\Minecraft\Minecraft\Java_1.12.2\IndustrialCraft",
    "p7": r"D:\tmp",
    "p8": r"D:\tmp\IndustrialCraft"
}


def zip_file(dir_path):
    with zipfile.ZipFile(dir_path + ".zip", "w", zipfile.ZIP_DEFLATED) as zfile:
        for iter_dir_path, dirs, files in os.walk(dir_path):
            for file in files:
                fpath = os.path.join(iter_dir_path, file)
                zfile.write(fpath)


def unzip_file(zip_file, target_dir):
    with zipfile.ZipFile(zip_file, "r") as zfile:
        for file in zfile.namelist():
            zfile.extract(file, target_dir)


def create_backup():
    os.chdir(pd.get("p7"))
    try:
        os.mkdir(pd.get("p8"))
    except FileExistsError:
        print("文件夹已经存在，跳过")
    cmd = "Xcopy " + pd.get("p1") + " " + pd.get("p8") + " /E/H/C/I"
    os.system(cmd)
    zip_file("IndustrialCraft")
    os.remove(pd.get("p4"))
    os.rename(pd.get("p3"), pd.get("p4"))
    shutil.move(pd.get("p5"), pd.get("p3"))


def rollback_new():
    if not os.path.exists(pd.get("p1")):
        print('未发现存档文件夹，已自动创建')
        os.mkdir(pd.get("p1"))
    else:
        cmd = 'RMDIR ' + pd.get("p1") + ' /S'
        os.system(cmd)
        unzip_file(pd.get("p3"), pd.get("p2"))
        shutil.move(pd.get("p6"), pd.get("p0"))


def rollback_old():
    if not os.path.exists(pd.get("p1")):
        print('未发现存档文件夹，已自动创建')
        os.mkdir(pd.get("p1"))
    else:
        cmd = 'RMDIR ' + pd.get("p1") + ' /S'
        os.system(cmd)
        unzip_file(pd.get("p4"), pd.get("p2"))
        shutil.move(pd.get("p6"), pd.get("p0"))


def menu():
    ui = """
    ----------------------------------------
    - 1. 创建备份   - 2. 还原备份    - 3. 退出
    ----------------------------------------
    """
    print(ui)
    opt = input("请选择操作")
    if int(opt) == 3:
        print('OJBK')
        exit()
    if int(opt) == 1:
        create_backup()
        print("备份成功")
        menu()
    elif int(opt) == 2:
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(pd.get("p3"))))
        time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(pd.get("p4"))))
        print('请选择备份时间进行还原:    a : {},   b : {}'.format(time1, time2))
        ver = input("请选择a / b    :")
        if ver.upper() == 'A':
            rollback_new()
            print('存档已恢复为({})版本'.format(time1))
            menu()
        if ver.upper() == 'B':
            rollback_old()
            print('存档已恢复为({})版本'.format(time2))
            menu()


if __name__ == '__main__':
    menu()
