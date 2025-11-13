"""
ComfyUI Kling Video Generation Nodes
Supports 4 versions: Standard (v1), Pro v1.0, Pro v1.6, and Master v2.0
"""
from .fal_utils import ApiHandler, ImageUtils


class KlingNode:
    """
    Kling Video Standard (v1) - Text-to-Video and Image-to-Video
    Cost-effective option for video generation.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "duration": (["5", "10"], {"default": "5"}),
                "aspect_ratio": (["16:9", "9:16", "1:1"], {"default": "16:9"}),
            },
            "optional": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_video"
    CATEGORY = "Kling/Video"

    def generate_video(self, prompt, duration, aspect_ratio, image=None):
        arguments = {
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
        }

        try:
            if image is not None:
                image_url = ImageUtils.upload_image(image)
                if image_url:
                    arguments["image_url"] = image_url
                    result = ApiHandler.submit_and_get_result(
                        "fal-ai/kling-video/v1/standard/image-to-video", arguments
                    )
                else:
                    return ApiHandler.handle_video_generation_error(
                        "kling-video/v1/standard", "Failed to upload image"
                    )
            else:
                result = ApiHandler.submit_and_get_result(
                    "fal-ai/kling-video/v1/standard/text-to-video", arguments
                )

            video_url = result["video"]["url"]
            return (video_url,)
        except Exception as e:
            return ApiHandler.handle_video_generation_error(
                "kling-video/v1/standard", str(e)
            )


class KlingPro10Node:
    """
    Kling Pro v1.0 - Enhanced quality with dual image support
    Supports both start and tail images for better control.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "duration": (["5", "10"], {"default": "5"}),
                "aspect_ratio": (["16:9", "9:16", "1:1"], {"default": "16:9"}),
            },
            "optional": {
                "image": ("IMAGE",),
                "tail_image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_video"
    CATEGORY = "Kling/Video"

    def generate_video(
        self, prompt, duration, aspect_ratio, image=None, tail_image=None
    ):
        arguments = {
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
        }

        try:
            if image is not None:
                image_url = ImageUtils.upload_image(image)
                if image_url:
                    arguments["image_url"] = image_url

                    # Handle tail image if provided
                    if tail_image is not None:
                        tail_image_url = ImageUtils.upload_image(tail_image)
                        if tail_image_url:
                            arguments["tail_image_url"] = tail_image_url
                        else:
                            return ApiHandler.handle_video_generation_error(
                                "kling-video/v1/pro", "Failed to upload tail image"
                            )

                    result = ApiHandler.submit_and_get_result(
                        "fal-ai/kling-video/v1/pro/image-to-video", arguments
                    )
                else:
                    return ApiHandler.handle_video_generation_error(
                        "kling-video/v1/pro", "Failed to upload image"
                    )
            else:
                result = ApiHandler.submit_and_get_result(
                    "fal-ai/kling-video/v1/pro/text-to-video", arguments
                )

            video_url = result["video"]["url"]
            return (video_url,)
        except Exception as e:
            return ApiHandler.handle_video_generation_error(
                "kling-video/v1/pro", str(e)
            )


class KlingPro16Node:
    """
    Kling Pro v1.6 - Latest Pro version with improved quality
    Supports both start and tail images.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "duration": (["5", "10"], {"default": "5"}),
                "aspect_ratio": (["16:9", "9:16", "1:1"], {"default": "16:9"}),
            },
            "optional": {
                "image": ("IMAGE",),
                "tail_image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_video"
    CATEGORY = "Kling/Video"

    def generate_video(
        self, prompt, duration, aspect_ratio, image=None, tail_image=None
    ):
        arguments = {
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
        }

        try:
            if image is not None:
                image_url = ImageUtils.upload_image(image)
                if image_url:
                    arguments["image_url"] = image_url

                    # Handle tail image if provided
                    if tail_image is not None:
                        tail_image_url = ImageUtils.upload_image(tail_image)
                        if tail_image_url:
                            arguments["tail_image_url"] = tail_image_url
                        else:
                            return ApiHandler.handle_video_generation_error(
                                "kling-video/v1.6/pro", "Failed to upload tail image"
                            )

                    result = ApiHandler.submit_and_get_result(
                        "fal-ai/kling-video/v1.6/pro/image-to-video", arguments
                    )
                else:
                    return ApiHandler.handle_video_generation_error(
                        "kling-video/v1.6/pro", "Failed to upload image"
                    )
            else:
                result = ApiHandler.submit_and_get_result(
                    "fal-ai/kling-video/v1.6/pro/text-to-video", arguments
                )

            video_url = result["video"]["url"]
            return (video_url,)
        except Exception as e:
            return ApiHandler.handle_video_generation_error(
                "kling-video/v1.6/pro", str(e)
            )


class KlingMasterNode:
    """
    Kling Master v2.0 - Highest quality model
    Premium tier for professional video generation.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": "", "multiline": True}),
                "duration": (["5", "10"], {"default": "5"}),
                "aspect_ratio": (["16:9", "9:16", "1:1"], {"default": "16:9"}),
            },
            "optional": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate_video"
    CATEGORY = "Kling/Video"

    def generate_video(self, prompt, duration, aspect_ratio, image=None):
        arguments = {
            "prompt": prompt,
            "duration": duration,
            "aspect_ratio": aspect_ratio,
        }

        try:
            if image is not None:
                image_url = ImageUtils.upload_image(image)
                if image_url:
                    arguments["image_url"] = image_url
                    result = ApiHandler.submit_and_get_result(
                        "fal-ai/kling-video/v2/master/image-to-video", arguments
                    )
                else:
                    return ApiHandler.handle_video_generation_error(
                        "kling-video/v2/master", "Failed to upload image"
                    )
            else:
                result = ApiHandler.submit_and_get_result(
                    "fal-ai/kling-video/v2/master/text-to-video", arguments
                )

            video_url = result["video"]["url"]
            return (video_url,)
        except Exception as e:
            return ApiHandler.handle_video_generation_error(
                "kling-video/v2/master", str(e)
            )


# Node mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "KlingStandard": KlingNode,
    "KlingPro10": KlingPro10Node,
    "KlingPro16": KlingPro16Node,
    "KlingMaster": KlingMasterNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "KlingStandard": "Kling Standard v1 (fal.ai)",
    "KlingPro10": "Kling Pro v1.0 (fal.ai)",
    "KlingPro16": "Kling Pro v1.6 (fal.ai)",
    "KlingMaster": "Kling Master v2.0 (fal.ai)",
}
