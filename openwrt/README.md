# How to add an lv_micropython package to the OnionIoT/source OpenWRT build system

Check out OnionIoT/source repo and build it. See instructions here: https://github.com/OnionIoT/source#using-this-build-system

Add lv_micropython to onion feed

```
mkdir ~/source/feeds/onion/lv_micropython
cp openwrt/Makefile ~/source/feeds/onion/lv_micropython/
```

Install the lv_micropython package

```
cd ~/source && ./scripts/feeds update onion && ./scripts/feeds install lv_micropython
```

Next enable the lv_micropython package. Two methods:

1. Use make menuconfig to select the lv_micropython package
2. Copy over a config file with the lv_micropython package selected:

```
cp openwrt/.config.O2-minimum ~/source/
cd ~/source && python scripts/onion-setup-build.py -c .config.O2-minimum
```

Build the package package (based on the latest from GitHub)

```
make package/lv_micropython/compile
```

To compile lv_micropython binary based on changes from a locally checked out lv_micropython repo:

```
# assuming repo checked out to ~/lv_micropython
make package/lv_micropython/clean ; make package/lv_micropython/prepare USE_SOURCE_DIR=~/lv_micropython V=99 ; make package/lv_micropython/compile V=99
```
