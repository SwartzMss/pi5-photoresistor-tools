# Pi5 光敏电阻示例

本仓库示范了如何在 Raspberry Pi 5 上使用光敏电阻测量环境光照强度。

## 接线

1. 将光敏电阻一端接至 3.3V。
2. 将光敏电阻另一端同时连接到 GPIO4 和电容器正端（0.1μF~1μF）。
3. 电容器的另一端接至 GND。
4. 所有地线需共地。

## 运行示例

确保已安装 `RPi.GPIO`，然后执行:

```bash
python3 read_photoresistor.py
```

脚本每秒打印一次测定的光照值。

## 文件

- `read_photoresistor.py` — 使用 GPIO4 读取光敏电阻的 Python 示例脚本
- `doc/device.jpg` — 实物照片，可供参考

## 实物照片

![device](doc/device.jpg)

## License

MIT
