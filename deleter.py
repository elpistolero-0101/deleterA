#!/usr/bin/env python3
import os
import subprocess
import sys

PASSWORD = "el_pistolero_root"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPresione ENTER para continuar...")

def header():
    print("DELETER 🗑️")
    print("=" * 30)

def run(cmd, root=False):
    try:
        if root:
            subprocess.run(["su", "-c", cmd])
        else:
            subprocess.run(cmd.split())
    except Exception as e:
        print("Error:", e)

def uninstall_safe():
    clear()
    header()
    pkg = input("Nombre del paquete (ej: com.android.chrome): ").strip()
    if not pkg:
        return
    print("\nDesinstalación segura")
    run(f"pm uninstall --user 0 {pkg}")
    pause()

def expert_mode():
    clear()
    header()
    print("⚠️ MODO EXPERTO – ELIMINACIÓN COMPLETA ⚠️\n")
    print("RIESGOS:")
    print("- Bootloop")
    print("- Android no inicia")
    print("- Brick del dispositivo")
    print("- Garantía anulada\n")

    if input("¿Continuar? (s/n): ").lower() != "s":
        return

    pwd = input("Contraseña Modo Experto: ")
    if pwd != PASSWORD:
        print("❌ Contraseña incorrecta")
        pause()
        return

    pkg = input("\nNombre del paquete EXACTO: ").strip()
    if not pkg:
        return

    if input(f"Escriba BORRAR para eliminar COMPLETAMENTE {pkg}: ") != "BORRAR":
        print("Cancelado")
        pause()
        return

    print("\nEliminando archivos del sistema...\n")

    run("mount -o rw,remount /system", root=True)
    run(f"rm -rf /system/app/{pkg}", root=True)
    run(f"rm -rf /system/priv-app/{pkg}", root=True)

    print("✅ Eliminación completa ejecutada")
    pause()

def system_apps_menu():
    while True:
        clear()
        header()
        print("APPS DEL SISTEMA ⚠️\n")
        print("1: Desinstalación segura")
        print("2: Modo experto – Eliminación completa 🔐")
        print("3: Volver\n")

        op = input("Seleccione opción: ")

        if op == "1":
            uninstall_safe()
        elif op == "2":
            expert_mode()
        elif op == "3":
            break

def normal_apps():
    clear()
    header()
    pkg = input("Nombre del paquete a desinstalar: ").strip()
    if pkg:
        run(f"pm uninstall {pkg}")
    pause()

def main_menu():
    while True:
        clear()
        header()
        print("1: Eliminar app normal")
        print("2: Eliminar apps del sistema")
        print("3: Salir\n")

        op = input("Seleccione qué desea hacer: ")

        if op == "1":
            normal_apps()
        elif op == "2":
            system_apps_menu()
        elif op == "3":
            sys.exit()
        else:
            pause()

if __name__ == "__main__":
    main_menu()
