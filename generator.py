import numpy as np
import cv2
import os
import datetime


def log(determine, img_path, new_path, noise_type, noisy_image, i):
    if determine:
        cv2.imwrite(f"{new_path}{noise_type}{i + 1}.jpg", noisy_image)
        print(
            f"✅ \033[92m[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\033[0m "
            f"\033[95m[old:{img_path}]\033[0m "
            f"\033[96m[new:{new_path}{noise_type}{i + 1}.jpg]\033[0m")
    else:
        print(
            f"❌ \033[91m[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"[old:{img_path}] "
            f"[new:{new_path}{noise_type}{i + 1}.jpg]\033[0m")


def gaussian(old_path, new_path, file, noise_type):
    """
    生成高斯噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            mean = np.random.uniform(30, 50)  # 随机均值
            stddev = np.random.uniform(30, 50)  # 随机标准差
            #  +---------------------------------------------------------------+
            height, width, channels = image.shape
            noise = np.random.normal(mean, stddev, (height, width, channels))
            noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def salt_and_pepper(old_path, new_path, file, noise_type):
    """
    生成椒盐噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            salt_prob = np.random.uniform(0, 0.05)  # 随机盐噪声强度
            pepper_prob = np.random.uniform(0, 0.05)  # 随机椒噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            total_pixels = image.size
            num_salt = int(total_pixels * salt_prob)
            salt_coordinates = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
            noisy_image[salt_coordinates[0], salt_coordinates[1], :] = 255
            num_pepper = int(total_pixels * pepper_prob)
            pepper_coordinates = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
            noisy_image[pepper_coordinates[0], pepper_coordinates[1], :] = 0
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def snow(old_path, new_path, file, noise_type):
    """
    生成雪花噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            snow_intensity = np.random.uniform(0, 0.01)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            num_snow_pixels = int(height * width * snow_intensity)
            for _ in range(num_snow_pixels):
                x, y = np.random.randint(0, width), np.random.randint(0, height)
                #  +---------------------------------------------------------------+
                noisy_image[y, x, :] = 255  # 雪花颜色[255白/0黑]
                #  +---------------------------------------------------------------+
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def spot(old_path, new_path, file, noise_type):
    """
    生成斑点噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            num_spots = np.random.randint(1000, 2000)  # 随机斑点数量
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            for _ in range(num_spots):
                x, y = np.random.randint(0, width), np.random.randint(0, height)
                for c in range(channels):
                    #  +---------------------------------------------------------------+
                    noisy_image[y, x, c] = np.random.uniform(0, 255)  # 随机斑点强度
                    #  +---------------------------------------------------------------+
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def corrugation(old_path, new_path, file, noise_type):
    """
    生成波纹噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            amplitude = np.random.uniform(10, 20)  # 随机振幅
            frequency = np.random.uniform(0, 0.2)  # 随机频率
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            x, y = np.meshgrid(np.arange(width), np.arange(height))
            wave_noise = amplitude * np.sin(2 * np.pi * frequency * x)
            wave_noise = np.dstack((wave_noise,) * channels)
            noisy_image = np.clip(noisy_image + wave_noise, 0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def poisson(old_path, new_path, file, noise_type):
    """
    生成泊松噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            noisy_image = np.copy(image)
            noisy_image = np.random.poisson(noisy_image).clip(0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def vague(old_path, new_path, file, noise_type):
    """
    生成模糊噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            kernel_size = (np.random.randint(5, 20), np.random.randint(5, 20))  # 随机内核大小
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])
            noisy_image = cv2.filter2D(noisy_image, -1, kernel)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def line(old_path, new_path, file, noise_type):
    """
    生成线条噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            num_lines = np.random.randint(0, 100)  # 随机线条数量
            line_length = (0, 10)  # 随机线条长度范围
            line_thickness = np.random.randint(0, 10)  # 随机线条宽度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            for _ in range(num_lines):
                x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
                x2, y2 = x1 + np.random.randint(*line_length), y1 + np.random.randint(*line_length)
                #  +---------------------------------------------------------------+
                color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))  # 随机线条颜色
                #  +---------------------------------------------------------------+
                thickness = line_thickness
                cv2.line(noisy_image, (x1, y1), (x2, y2), color, thickness)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def color(old_path, new_path, file, noise_type):
    """
    生成彩色噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            noise_intensity = np.random.uniform(50, 200)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            noise = np.random.randint(-noise_intensity, noise_intensity, (height, width, channels))
            noisy_image = np.clip(noisy_image + noise, 0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def gradient(old_path, new_path, file, noise_type):
    """
    生成渐变噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            gradient_intensity = np.random.uniform(20, 200)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            gradient_noise = np.zeros((height, width, channels), dtype=np.uint8)
            for c in range(channels):
                gradient = np.linspace(0, gradient_intensity, width)
                gradient = gradient.astype(np.uint8)
                gradient_noise[:, :, c] = gradient
            noisy_image = cv2.add(noisy_image, gradient_noise)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def uniform(old_path, new_path, file, noise_type):
    """
    生成均匀噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            noise_intensity = np.random.uniform(1, 3)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            noise = np.random.uniform(-noise_intensity, noise_intensity, (height, width, channels)).astype(np.uint8)
            noisy_image = cv2.add(noisy_image, noise)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def banding(old_path, new_path, file, noise_type):
    """
    生成色带噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            num_strips = np.random.randint(1, 20)  # 随机色带数量
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            for _ in range(num_strips):
                #  +---------------------------------------------------------------+
                stripe_width = np.random.randint(1, 5)  # 随机色带宽度
                direction = np.random.randint(0, 2)  # 随机水平/垂直
                #  +---------------------------------------------------------------+
                color = np.random.randint(0, 256, (channels,))
                if direction == 0:
                    x = np.random.randint(0, width - stripe_width)
                    noisy_image[:, x:x + stripe_width, :] = color
                else:
                    y = np.random.randint(0, height - stripe_width)
                    noisy_image[y:y + stripe_width, :, :] = color
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def stacking(old_path, new_path, file, noise_type):
    """
    生成堆叠噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            num_layers = np.random.randint(1, 3)  # 随机堆叠图层数量
            noise_intensity = np.random.uniform(1, 3)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            for _ in range(num_layers):
                height, width, _ = image.shape
                noise_layer = np.random.randint(-noise_intensity, noise_intensity, (height, width, 3)).astype(np.uint8)
                noisy_image = cv2.add(noisy_image, noise_layer)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def shadow(old_path, new_path, file, noise_type):
    """
    生成阴影噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            num_shadows = np.random.randint(1, 50)  # 阴影数量
            shadow_intensity = np.random.uniform(1, 30)  # 阴影强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            for _ in range(num_shadows):
                x = np.random.randint(0, width)
                y = np.random.randint(0, height)
                shadow_height = np.random.randint(10, 50)
                shadow_width = np.random.randint(10, 50)
                intensity = np.random.randint(shadow_intensity, 256)
                noisy_image[y:y + shadow_height, x:x + shadow_width, :] -= intensity
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def scanline(old_path, new_path, file, noise_type):
    """
    生成扫描线噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            num_lines = np.random.randint(5, 20)  # 随机扫描线的数量
            line_thickness = np.random.randint(1, 3)  # 随机扫描线的宽度
            line_color = (0, 0, 0)  # 扫描线的颜色
            orientation = 'horizontal'  # 扫描线的方向[horizontal水平/vertical垂直]
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            for _ in range(num_lines):
                if orientation == 'horizontal':
                    y = np.random.randint(0, height)
                    cv2.line(noisy_image, (0, y), (width, y), line_color, line_thickness)
                elif orientation == 'vertical':
                    x = np.random.randint(0, width)
                    cv2.line(noisy_image, (x, 0), (x, height), line_color, line_thickness)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def jitter(old_path, new_path, file, noise_type):
    """
    生成震动噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            max_displacement = 50  # 最大平移距离
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            displacement_x = np.random.randint(-max_displacement, max_displacement)
            displacement_y = np.random.randint(-max_displacement, max_displacement)
            M = np.float32([[1, 0, displacement_x], [0, 1, displacement_y]])
            noisy_image = cv2.warpAffine(noisy_image, M, (width, height))
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def silhouette(old_path, new_path, file, noise_type):
    """
    生成剪影噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            contrast_factor = np.random.uniform(1, 2)  # 随机对比度因子
            brightness_factor = np.random.uniform(5, 10)  # 随机亮度因子
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            noisy_image = noisy_image * contrast_factor + brightness_factor
            noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def lens_flare(old_path, new_path, file, noise_type):
    """
    生成镜头光晕噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            num_flares = np.random.randint(1, 5)  # 随机光晕数量
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            for _ in range(num_flares):
                #  +---------------------------------------------------------------+
                flare_intensity = np.random.uniform(0, 0.5)  # 随机光晕强度
                #  +---------------------------------------------------------------+
                x = np.random.randint(0, width)
                y = np.random.randint(0, height)
                flare_color = (np.random.randint(200, 256), np.random.randint(200, 256), np.random.randint(200, 256))
                flare_image = np.zeros((height, width, channels), dtype=np.uint8)
                cv2.circle(flare_image, (x, y), np.random.randint(10, 100), flare_color, -1)
                noisy_image = cv2.addWeighted(noisy_image, 1 - flare_intensity, flare_image, flare_intensity, 0)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def light_scattering(old_path, new_path, file, noise_type):
    """
    生成光线散射噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            #  +---------------------------------------------------------------+
            num_scatters = np.random.randint(1, 20)  # 随机散射光线数量
            scatter_length = np.random.randint(100, 200)  # 随机散射光线长度
            scatter_color = (
                np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))  # 随机散射光线强度
            #  +---------------------------------------------------------------+
            for _ in range(num_scatters):
                x1, y1 = np.random.randint(0, width), np.random.randint(0, height)
                x2, y2 = x1 + scatter_length, y1 + scatter_length
                scatter_color = (np.random.randint(200, 256), np.random.randint(200, 256), np.random.randint(200, 256))
                cv2.line(noisy_image, (x1, y1), (x2, y2), scatter_color, np.random.randint(1, 5))
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def grid(old_path, new_path, file, noise_type):
    """
    生成网格噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            grid_spacing = np.random.randint(10, 100)  # 随机网格间距
            line_thickness = np.random.randint(1, 2)  # 随机网格线宽度
            line_color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))  # 随机网格线颜色
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            for x in range(0, width, grid_spacing):
                cv2.line(noisy_image, (x, 0), (x, height), line_color, line_thickness)
            for y in range(0, height, grid_spacing):
                cv2.line(noisy_image, (0, y), (width, y), line_color, line_thickness)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def gamma(old_path, new_path, file, noise_type):
    """
    生成伽马噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            gamma_shape = np.random.randint(2, 20)  # 随机伽马分布的形状
            gamma_scale = np.random.randint(2, 20)  # 随机伽马分布的尺度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            gamma_noise = np.random.gamma(gamma_shape, gamma_scale, (height, width, channels)).astype(np.uint8)
            noisy_image = cv2.add(noisy_image, gamma_noise)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def multiplicative(old_path, new_path, file, noise_type):
    """
    生成乘性噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            intensity = np.random.uniform(0, 0.5)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            noise = np.random.normal(1.0, intensity, image.shape).astype(np.float32)
            noisy_image = np.multiply(noisy_image, noise)
            noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def rayleigh(old_path, new_path, file, noise_type):
    """
    生成瑞利噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            scale = np.random.uniform(5, 30)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            rayleigh_noise = np.random.rayleigh(scale, image.shape).astype(np.float32)
            noisy_image = np.add(noisy_image, rayleigh_noise)
            noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def exponential(old_path, new_path, file, noise_type):
    """
    生成指数分布噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            scale = np.random.uniform(5, 30)  # 随机噪声强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            exponential_noise = np.random.exponential(scale, image.shape).astype(np.float32)
            noisy_image = np.add(noisy_image, exponential_noise)
            noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def granular(old_path, new_path, file, noise_type):
    """
    生成散粒噪声
    """
    noisy_image = None
    for i in range(len(file)):
        img_path = old_path + file[i]
        try:
            image = cv2.imread(img_path)
            #  +---------------------------------------------------------------+
            grain_density = np.random.uniform(0, 0.5)  # 随机散粒密度
            grain_intensity = np.random.uniform(20, 100)  # 随机散粒强度
            #  +---------------------------------------------------------------+
            noisy_image = np.copy(image)
            height, width, channels = image.shape
            num_grains = int(grain_density * height * width)
            for _ in range(num_grains):
                x = np.random.randint(0, width)
                y = np.random.randint(0, height)
                noise_color = (np.random.randint(0, grain_intensity), np.random.randint(0, grain_intensity),
                               np.random.randint(0, grain_intensity))
                noisy_image[y, x, :] = np.add(noisy_image[y, x, :], noise_color)
            log(1, img_path, new_path, noise_type, noisy_image, i)
        except:
            log(0, img_path, new_path, noise_type, noisy_image, i)


def main(old_path, new_path, noise_type):
    """
    给图片加上噪声
    :param old_path:旧图片地址
    :param new_path:新图片地址
    :param noise_type:噪声类型
    """
    os.makedirs(new_path, exist_ok=True)
    file = os.listdir(old_path)
    if noise_type == "gaussian":
        gaussian(old_path, new_path, file, noise_type)
    if noise_type == "salt_and_pepper":
        salt_and_pepper(old_path, new_path, file, noise_type)
    if noise_type == "snow":
        snow(old_path, new_path, file, noise_type)
    if noise_type == "spot":
        spot(old_path, new_path, file, noise_type)
    if noise_type == "corrugation":
        corrugation(old_path, new_path, file, noise_type)
    if noise_type == "poisson":
        poisson(old_path, new_path, file, noise_type)
    if noise_type == "vague":
        vague(old_path, new_path, file, noise_type)
    if noise_type == "line":
        line(old_path, new_path, file, noise_type)
    if noise_type == "color":
        color(old_path, new_path, file, noise_type)
    if noise_type == "gradient":
        gradient(old_path, new_path, file, noise_type)
    if noise_type == "uniform":
        uniform(old_path, new_path, file, noise_type)
    if noise_type == "banding":
        banding(old_path, new_path, file, noise_type)
    if noise_type == "stacking":
        stacking(old_path, new_path, file, noise_type)
    if noise_type == "shadow":
        shadow(old_path, new_path, file, noise_type)
    if noise_type == "scanline":
        scanline(old_path, new_path, file, noise_type)
    if noise_type == "jitter":
        jitter(old_path, new_path, file, noise_type)
    if noise_type == "silhouette":
        silhouette(old_path, new_path, file, noise_type)
    if noise_type == "lens_flare":
        lens_flare(old_path, new_path, file, noise_type)
    if noise_type == "light_scattering":
        light_scattering(old_path, new_path, file, noise_type)
    if noise_type == "grid":
        grid(old_path, new_path, file, noise_type)
    if noise_type == "gamma":
        gamma(old_path, new_path, file, noise_type)
    if noise_type == "multiplicative":
        multiplicative(old_path, new_path, file, noise_type)
    if noise_type == "rayleigh":
        rayleigh(old_path, new_path, file, noise_type)
    if noise_type == "exponential":
        exponential(old_path, new_path, file, noise_type)
    if noise_type == "granular":
        granular(old_path, new_path, file, noise_type)


if __name__ == '__main__':
    """
    高斯:gaussian
    椒盐:salt_and_pepper
    雪花:snow
    斑点:spot
    波纹:corrugation
    泊松:poisson
    模糊:vague
    线条:line
    彩色:color
    渐变:gradient
    均匀:uniform
    色带:banding
    堆叠:stacking
    阴影:shadow
    扫描线:scanline
    震动:jitter
    剪影:silhouette
    镜头光晕:lens_flare
    光线散射:light_scattering
    网格:grid
    伽马:gamma
    乘性:multiplicative
    瑞利:rayleigh
    指数分布:exponential
    散粒:granular
    """
    noise = "gaussian"  # 选择噪声类型
    main("./image/", f"./noise_image/", noise)  # 路径结尾处请加上/
