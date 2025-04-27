from flask import Flask, request, jsonify
import time

class TimingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Before Request Logic
        start_time = time.time()
        print("🚀 [Middleware] Before Request:")
        print(f"Method: {environ['REQUEST_METHOD']}")
        print(f"Path: {environ['PATH_INFO']}")
        print("-------------")

        def custom_start_response(status, headers, exc_info=None):
            # After Request Logic
            duration = time.time() - start_time
            print("✅ [Middleware] After Request:")
            print(f"Status: {status}")
            print(f"Response Headers: {headers}")
            print(f"Duration: {duration:.4f} seconds")
            print("-------------")
            return start_response(status, headers, exc_info)

        # Call the actual application
        return self.app(environ, custom_start_response)


