# from pathlib import Path

# fake_path = Path("C:/this/does/not/exist")
# print(bool(fake_path))  # True! (object exists, even if file doesn't)

# real_path = Path("C:/Users")
# print(bool(real_path))  # Also True

# # Correct check:
# print(fake_path.exists())  # False
# print(real_path.exists())  # True

# import threading
# import time
# from threading import Lock

# # Simple example: I/O-bound operation
# counter = 0


# def increment_counter(thread_id):
#     global counter
#     for _ in range(10000):
#           # Acquire lock
#         counter += 1
#             # Critical section: counter is safe here
#         time.sleep(0.001)
#         # Lock released automatically
#     print(f"Thread {thread_id} finished")

# # Create and start threads
# threads = []
# for i in range(3):
#     thread = threading.Thread(target=increment_counter, args=(i,))
#     thread.start()
#     threads.append(thread)

# # Wait for all threads to complete
# for thread in threads:
#     thread.join()

# print(f"Final counter: {counter}")  # Will be 3000000 (correct)

# import threading
# import time

# counter = 0
# lock = threading.Lock()

# def increment_counter(thread_id):
#     global counter
#     for _ in range(100000):  # Increased iteration size
#         # 1. Read the current value
#         with lock:
#             current_val = counter 
            
             
            
#             # 3. Modify and Write
#             counter = current_val + 1

#     print(f"Thread {thread_id} finished")

# threads = []
# for i in range(3):
#     thread = threading.Thread(target=increment_counter, args=(i,))
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()

# # Expected math: 3 * 100,000 = 300,000
# print(f"Final counter: {counter}")

# from multiprocessing import Process, Queue, Pool
# import time

# # Method 1: Manual process creation
# def cpu_intensive_task(n, queue):
#     """CPU-bound task: Calculate sum of squares"""
#     result = sum(i**2 for i in range(n))
#     queue.put(result)  # Send result back to parent
#     print(f"Process {Process().pid} completed")

# if __name__ == '__main__':  # Required for Windows
#     queue = Queue()
    
#     # Create multiple processes
#     processes = []
#     for i in range(3):
#         p = Process(target=cpu_intensive_task, args=(100, queue))
#         p.start()
#         processes.append(p)
    
#     # Collect results
#     results = []
#     for _ in range(3):
#         result = queue.get()  # Blocking call
#         results.append(result)
    
#     # Wait for processes to finish
#     for p in processes:
#         p.join()
    
#     print(f"Results: {results}")

# # Method 2: Process Pool (simpler)
# def compute_task(n):
#     """CPU-bound task"""
#     return sum(i**2 for i in range(n))

# if __name__ == '__main__':
#     with Pool(processes=4) as pool:
#         results = pool.map(compute_task, [100] * 10)
#         print(f"Results: {results}")

# import asyncio

# async def fetch_data():
#     print("Fetching...")
#     return {"data": 123}

# # Calling the function normally
# result = fetch_data()

# print(type(result))
# print(result)


import base64
import io
import requests
from PIL import Image

# 1. Configuration
# Replace with your actual NVIDIA API key from build.nvidia.com
NVIDIA_API_KEY = "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"

# Corrected Endpoint with literal dot (.) for FLUX.1-dev
API_URL = "https://ai.api.nvidia.com/v1/genai/black-forest-labs/flux.1-dev"

headers = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

# Payload conforming exactly to NVIDIA's schema
payload = {
    "prompt": "A boy cycling beside a river ramp and dusk time and face towards camera and smiling, ultra-realistic, 8k resolution",
    "height": 1024,
    "width": 1024,
    "cfg_scale": 5,
    "mode": "base",  # Specifies text-to-image mode
    "samples": 1,
    "seed": 0,
    "steps": 50
}

print("Sending request to NVIDIA NIM...")

# 2. Call the API
response = requests.post(API_URL, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()

    try:
        # 3. Visual NIMs return base64 strings under 'artifacts'
        b64_string = response_data["artifacts"][0]["base64"]

        # 4. Decode the Base64 string into binary bytes
        image_bytes = base64.b64decode(b64_string)

        # 5. Convert bytes into a viewable image object using PIL
        image = Image.open(io.BytesIO(image_bytes))

        # 6. Save the output image locally
        output_filename = "flux_output.png"
        image.save(output_filename)

        print(f"Success! Image saved as '{output_filename}'")
        image.show()

    except (KeyError, IndexError):
        # Fallback print if the schema structure differs across catalog adjustments
        print("Failed to parse 'artifacts'. Printing structure keys:")
        print(response_data.keys())
else:
    print(f"Error {response.status_code}: {response.text}")