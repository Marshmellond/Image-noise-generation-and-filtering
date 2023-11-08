<div align="center"><img src="https://s2.loli.net/2023/11/08/yhqKHotF4Rk3276.jpg"></div>
<div align="center"><h1>图片噪声生成与滤波</h1></div>

## 先看效果

<a href="https://smms.app/image/SQ3YhrsePCno2E8" target="_blank"><img src="https://s2.loli.net/2023/11/08/SQ3YhrsePCno2E8.jpg" ></a>
<a href="https://smms.app/image/Um1zMvlkgSGsC26" target="_blank"><img src="https://s2.loli.net/2023/11/08/Um1zMvlkgSGsC26.jpg" ></a>
<a href="https://smms.app/image/v1AdDPwUX2siBQW" target="_blank"><img src="https://s2.loli.net/2023/11/08/v1AdDPwUX2siBQW.jpg" ></a>
<a href="https://smms.app/image/WqQs3t9KeDYyGNu" target="_blank"><img src="https://s2.loli.net/2023/11/08/WqQs3t9KeDYyGNu.jpg" ></a>
<a href="https://smms.app/image/AlbG51L7mHcEFpQ" target="_blank"><img src="https://s2.loli.net/2023/11/08/AlbG51L7mHcEFpQ.jpg" ></a>
<a href="https://smms.app/image/S7rJVMxYD9qPcbd" target="_blank"><img src="https://s2.loli.net/2023/11/08/S7rJVMxYD9qPcbd.jpg" ></a>
<a href="https://smms.app/image/IXeQnAiEHp1tZ4o" target="_blank"><img src="https://s2.loli.net/2023/11/08/IXeQnAiEHp1tZ4o.jpg" ></a>
<a href="https://smms.app/image/5TD6lOSU8ABHjQy" target="_blank"><img src="https://s2.loli.net/2023/11/08/5TD6lOSU8ABHjQy.jpg" ></a>
<a href="https://smms.app/image/DoU43ZETNzI6vmQ" target="_blank"><img src="https://s2.loli.net/2023/11/08/DoU43ZETNzI6vmQ.jpg" ></a>
<a href="https://smms.app/image/uAUOJ3ZyRbMeK7G" target="_blank"><img src="https://s2.loli.net/2023/11/08/uAUOJ3ZyRbMeK7G.jpg" ></a>
<a href="https://smms.app/image/KNmHhpuCU9LxSEG" target="_blank"><img src="https://s2.loli.net/2023/11/08/KNmHhpuCU9LxSEG.jpg" ></a>
<a href="https://smms.app/image/hsB162jdQHwReT9" target="_blank"><img src="https://s2.loli.net/2023/11/08/hsB162jdQHwReT9.jpg" ></a>
<a href="https://smms.app/image/b9UWQDveXlcpCyK" target="_blank"><img src="https://s2.loli.net/2023/11/08/b9UWQDveXlcpCyK.jpg" ></a>
<a href="https://smms.app/image/LaZMIGF75UfNDAb" target="_blank"><img src="https://s2.loli.net/2023/11/08/LaZMIGF75UfNDAb.jpg" ></a>
<a href="https://smms.app/image/geMk9K7c8AUDBFE" target="_blank"><img src="https://s2.loli.net/2023/11/08/geMk9K7c8AUDBFE.jpg" ></a>

## 支持生成噪声

- 高斯: gaussian
- 椒盐: salt_and_pepper
- 雪花: snow
- 斑点: spot
- 波纹: corrugation
- 泊松: poisson
- 模糊: vague
- 线条: line
- 彩色: color
- 渐变: gradient
- 均匀: uniform
- 色带: banding
- 堆叠: stacking
- 阴影: shadow
- 扫描线: scanline
- 震动: jitter
- 剪影: silhouette
- 镜头光晕: lens_flare
- 光线散射: light_scattering
- 网格: grid
- 伽马: gamma
- 乘性: multiplicative
- 瑞利: rayleigh
- 指数分布: exponential
- 散粒: granular


## 环境

- python
- cv2

## 开始使用
```shell
│  filterate.py   # 傻狗
│  generator.py   # 你妈死了
│  LICENSE
│  README.md
│
├─.idea
│  │  .gitignore
│  │  image-noise-generation-and-filtering.iml
│  │  misc.xml
│  │  modules.xml
│  │  vcs.xml
│  │  workspace.xml
│  │
│  └─inspectionProfiles
│          profiles_settings.xml
│          Project_Default.xml
│
├─image
│      demo.jpg
│
└─noise_image
```
-- 