<div align="center"><img src="https://s2.loli.net/2023/11/08/yhqKHotF4Rk3276.jpg"></div>
<div align="center"><h1>图片噪声生成</h1></div>

## 先看效果

<p>
<img src="https://s2.loli.net/2023/11/08/SQ3YhrsePCno2E8.jpg" />
<img src="https://s2.loli.net/2023/11/08/Um1zMvlkgSGsC26.jpg" />
<img src="https://s2.loli.net/2023/11/08/v1AdDPwUX2siBQW.jpg" />
<img src="https://s2.loli.net/2023/11/08/WqQs3t9KeDYyGNu.jpg" />
<img src="https://s2.loli.net/2023/11/08/S7rJVMxYD9qPcbd.jpg" />
<img src="https://s2.loli.net/2023/11/08/IXeQnAiEHp1tZ4o.jpg" />
<img src="https://s2.loli.net/2023/11/08/5TD6lOSU8ABHjQy.jpg" />
<img src="https://s2.loli.net/2023/11/08/DoU43ZETNzI6vmQ.jpg" />
<img src="https://s2.loli.net/2023/11/08/uAUOJ3ZyRbMeK7G.jpg" />
<img src="https://s2.loli.net/2023/11/08/KNmHhpuCU9LxSEG.jpg" />
<img src="https://s2.loli.net/2023/11/08/hsB162jdQHwReT9.jpg" />
<img src="https://s2.loli.net/2023/11/08/b9UWQDveXlcpCyK.jpg" />
<img src="https://s2.loli.net/2023/11/08/DMuoyizcUWBIgJY.jpg" />
<img src="https://s2.loli.net/2023/11/08/geMk9K7c8AUDBFE.jpg" />
<img src="https://s2.loli.net/2023/11/08/LaZMIGF75UfNDAb.jpg" />
</p>


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

- python3
- numpy
- cv2

## 项目结构

```shell
┌Project
├─image  源文件夹
│      demo.jpg  示例图片
│  generator.py  生成噪声
└─noise_image  噪声文件夹
```
