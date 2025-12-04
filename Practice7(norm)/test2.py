import cv2
import numpy as np

def load_images(original_path, distorted_path):
    """Загружает и подгоняет размеры изображений"""
    original = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    distorted = cv2.imread(distorted_path, cv2.IMREAD_GRAYSCALE)
    
    if original is None or distorted is None:
        raise ValueError("Не удалось загрузить изображения")
    
    
    if original.shape != distorted.shape:
        distorted = cv2.resize(distorted, (original.shape[1], original.shape[0]))
    
    return original, distorted

def calculate_mse(original, distorted):
    """Среднеквадратичная ошибка"""
    return np.mean((original.astype(float) - distorted.astype(float)) ** 2)

def calculate_psnr(original, distorted):
    """Пиковое отношение сигнал/шум"""
    mse = calculate_mse(original, distorted)
    if mse == 0:
        return float('inf')
    
    return 20 * np.log10(255.0 / np.sqrt(mse))

def simple_analysis(original_path, distorted_path):
    """Простой анализ двух изображений"""
    print("="*60)
    print("ЗАДАНИЕ 2: РАБОТА СБИТНЕВОЙ ДАРЬИ".center(60))
    print("="*60)
    print("АНАЛИЗ ИСКАЖЕНИЙ ИЗОБРАЖЕНИЙ".center(60))
    print("="*60)
    
    try:


        original, distorted = load_images(original_path, distorted_path)

        mse = calculate_mse(original, distorted)
        psnr = calculate_psnr(original, distorted)
        
        print(f"\nРЕЗУЛЬТАТЫ АНАЛИЗА:")
        print(f"MSE (Среднеквадратичная ошибка): {mse:.2f}")
        print(f"PSNR (Отношение сигнал/шум): {psnr:.2f} dB")





        if psnr > 40:
            print("✅ Отличное качество (PSNR > 40 dB)")
        elif psnr > 30:
            print("👍 Хорошее качество (PSNR 30-40 dB)")
        elif psnr > 20:
            print("⚠️  Среднее качество (PSNR 20-30 dB)")
        else:
            print("❌ Низкое качество (PSNR < 20 dB)")




        diff = cv2.absdiff(original, distorted)
        print(f"\nАНАЛИЗ РАЗЛИЧИЙ:")
        print(f"Максимальная разница: {np.max(diff)} пикселей")
        print(f"Средняя разница: {np.mean(diff):.2f} пикселей")
        print(f"Общее количество пикселей: {original.size}")
        
    except Exception as e:
        print(f"\nОШИБКА: {e}")




if __name__ == "__main__":
    print("\n" + "="*60)
    print("ПРОГРАММА АНАЛИЗА ИСКАЖЕНИЙ ИЗОБРАЖЕНИЙ".center(60))
    print("="*60)
    print("\nИСПОЛЬЗОВАНИЕ:")
    print("1. Положите два изображения в папку с программой")
    print("2. Вызовите функцию: simple_analysis('файл1.jpg', 'файл2.jpg')")
    print("3. Получите оценку искажений")
    print("\n" + "-"*60)



    print("ТЕСТОВЫЙ ПРИМЕР".center(60))
    print("-"*60)





    test_img = np.ones((100, 100), dtype=np.uint8) * 128
    test_img[30:70, 30:70] = 200




    noise = np.random.randint(0, 50, (100, 100))
    noisy_img = cv2.add(test_img, noise.astype(np.uint8))



    cv2.imwrite("test_orig.png", test_img)
    cv2.imwrite("test_noise.png", noisy_img)
    
    simple_analysis("test_orig.png", "test_noise.png")
    
    print("\n" + "="*60)
    print("АНАЛИЗ ЗАВЕРШЕН".center(60))
    print("="*60)
    
    
            
        
        