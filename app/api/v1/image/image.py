#!/usr/bin/python
# -*- coding: utf-8 -*-
# jxb3019
# feature:

from datetime import datetime, timedelta
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.models.image.image_brightness import enhance_brightness

router = APIRouter()

@router.post("/image_enhance", summary="图像亮度提升")
async def image_enhance(request: Request):
    try:
        data = await request.json()
        input_path = data["inputPath"]
        output_path = data["outputPath"]
        brightness_factor = float(data["brightnessFactor"])
        user_name = data["name"]
        
        # 图像处理
        # enhance_brightness(input_path, output_path, brightness_factor)
        print(1)
        response = {
            "status": "success",
            "message": "图像处理成功",
        }
        # 处理成功并返回成功的响应
        print(JSONResponse(content=response))
        return JSONResponse(content=response)
    
    except Exception as e:
        # 处理过程中发生错误，返回错误的响应
        response={"message": "图像处理失败"+e,"status":"fail"}
        return JSONResponse(content=response)

