# api_fb_scraping_docker


## Description

This project is a guide to build a scraping service using fastAPI and facebook_page_scraper, then store the scraping data in MongoDB, and finally dockerize it.

## Docker 

After cloning this repo, run the following command to start all the services defined in docker-compose.yml which are 'scraping service' and 'mongodb'.
```bash
sudo docker-compose up
```

## Details & Outputs

- To test the service, we created a Facebook page Generalsoftwareengineeringposts containing 10 posts.


- We created a GET HTTP method to start the scraping of the mentioned FB page. The output of "http://127.0.0.1:8008/default_scraping" is:

```bash
[
  "{\"pfbid02jZNYtix1Vu3ocetkE7QDQ1tZCvko5vNQ5AnirvTPvDWsv3K89yQdPQhQyYknGvXMl\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"PHP is widely used for server-side web development, when a website frequently requests information from a server. As an older language, PHP benefits from a large ecosystem of users who have produced frameworks, libraries, and automation tools to make the programming language easier to use. PHP code is also easy to debug.Source: https://www.northeastern.edu/.../most-popular.../\", \"posted_on\": \"2022-08-30T07:12:34.648493\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid02jZNYtix1Vu3ocetkE7QDQ1tZCvko5vNQ5AnirvTPvDWsv3K89yQdPQhQyYknGvXMl&id=102394349277873&__cft__[0]=AZX7aqRfUCB4kOdXkQL2x2Dpo_FjaLZUathrdnmP6dv_qOQZi8aWJPGcYNInTTKbJ0sw-OVOqffVU3j3KIqOGInukc3VXS6blE_LislHdpQeghb9SdcF_Sjfstcnq5uGvj-SPuEbZYWyu99Y6e5CpEJ5YSAIjDTYMaq1L8g5alYf33XHCesP2N3FXpj8IMH5hP0cpZnzFd7zb2Db5e9F9ScY&__tn__=%2CO%2CP-R\"}, \"pfbid02LotwHKt4n2UTdkxUnoxwHpbF23mQgGbYhEXAXTe9WRFWkts2ZjPkRJ4sTWxdFm1jl\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"Swift is Apple’s language for developing applications for Mac computers and Apple’s mobile devices, including the iPhone, iPad, and Apple Watch. Like many modern programming languages, Swift has a highly readable syntax, runs code quickly, and can be used for both client-side and server-side development. Source: https://www.northeastern.edu/.../most-popular.../\", \"posted_on\": \"2022-08-30T07:53:34.719371\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid02LotwHKt4n2UTdkxUnoxwHpbF23mQgGbYhEXAXTe9WRFWkts2ZjPkRJ4sTWxdFm1jl&id=102394349277873&__cft__[0]=AZU8d4y8XphmXHt_l02mkz1kK559msfGFJEzu0gDwHXi-hQYteiR47M8PVu8n2R-Xa2GqcQ9Hxh56pBWp9nqe_mfn2PvmwSk3-lFw_KCFn3k9yay7Yw6AuZlymnyt3f95y-X0Pp-K7zTlBNQyeUMK1gN7Tia1aFcZvHBo2rVV8QF3r0QG_zEul_QqEp_7QRtIOvQ7pcld24TFIIHtYr3p9_N&__tn__=%2CO%2CP-R\"}, \"pfbid02aX483iU2Q43fBiLtkum331NYo8rhLVinTMTxy8dVN7PXKvXZSsu8aHNXBNfVZMb3l\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"R is heavily used in statistical analytics and machine learning applications. The language is extensible and runs on many operating systems. Many large companies have adopted R in order to analyze their massive data sets, so programmers who know R are in great demand. Source: https://www.northeastern.edu/.../most-popular.../\", \"posted_on\": \"2022-08-30T07:53:34.786311\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid02aX483iU2Q43fBiLtkum331NYo8rhLVinTMTxy8dVN7PXKvXZSsu8aHNXBNfVZMb3l&id=102394349277873&__cft__[0]=AZV647g1CMdg9wVr7Z3Dfa47chgqFxtvW8U6bSopQaB2wO9NzLMQK_uErN9ChD6J-ZMmtMLeNnSRhMKFIHCS9ouZeVE6mNEENfUIhW-mr6ygsS-O174cXhw0nHhu-nnmbc2XnqIKAmsjn7gN2XYw-Wzp3QreNV4mM_TpCxYi5jlEJjRHyrB5BPn_NcVBI64NbpM_X2-vTQ7u3s73BSH0ygve&__tn__=%2CO%2CP-R\"}, \"pfbid02cmT97hcvsaViCdUVVQhHADqVN6UoFzWsTbvHkJc9tNMAUPzGeT2jaWUcymRCoQvXl\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"Also referred to as Golang, Go was developed by Google to be an efficient, readable, and secure language for system-level programming. It works well for distributed systems, in which systems are located on different networks and need to communicate by sending messages to each other. While it is a relatively new language, Go has a large standards library and extensive documentation.Source: https://www.northeastern.edu/.../most-popular.../\", \"posted_on\": \"2022-08-30T07:54:34.859120\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid02cmT97hcvsaViCdUVVQhHADqVN6UoFzWsTbvHkJc9tNMAUPzGeT2jaWUcymRCoQvXl&id=102394349277873&__cft__[0]=AZWl6MOkGf1C225oZJY-vqZulO-lakdeq4H1fduXDsJB3rmy0XBwccGBtGCpJBmLDP7KHtQeH_m0pGbpEeXekJ3hdQtb6QQjZ_G3k-pEPIe9xih9uwUl_B1IPmhvGqC-IJrucdJWACXRIiEkhXJ1rgWyfN1vhlw902ulY6r2R4v2juASvKDjHYhyePsE0heqLDrH_jDxj5qMwYK1KVAnIYfE&__tn__=%2CO%2CP-R\"}, \"pfbid0mcJYEekjvo64k52uXNwgWpmnqjwuwL5waXtDyXEap6g2d6gcPzgSTULPd7WGELF8l\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"C++ is an extension of C that works well for programming the systems that run applications, as opposed to the applications themselves. C++ also works well for multi-device and multi-platform systems. Over time, programmers have written a large set of libraries and compilers for C++. Being able to use these utilities effectively is just as important to understanding a programming language as writing code, Gorton says.Source: https://www.northeastern.edu/.../most-popular.../… See more\", \"posted_on\": \"2022-08-30T07:54:35.733397\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid0mcJYEekjvo64k52uXNwgWpmnqjwuwL5waXtDyXEap6g2d6gcPzgSTULPd7WGELF8l&id=102394349277873&__cft__[0]=AZVnUPbi4Zs_aNmgq7QenAvAYunm-atDDlowPdf6yNj1OXcJigFOEl2niTLvrfu7fBH574vFFbThpxgLcUNinvj9VEv_qYw7MtdMPzNrp1U966iFRkou45J3C7B3KCSkx-Yd5uLibElLYY10x6vQyKK2sB9x7dXJbT7Wz57kVgTayuQxkTZbTva4HUH0oK3inFHMGT1xGM0ppu9lbL51z6Ia&__tn__=%2CO%2CP-R\"}, \"pfbid02UUbidMXFG92kTrtFn2wDtf7sYzwVr3LFMCrsFAMpyjt6FrV9jjn5m72cP1QX7ehrl\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"Along with Python and Java, C forms a “good foundation” for learning how to program, Gorton says. As one of the first programming languages ever developed, C has served as the foundation for writing more modern languages such as Python, Ruby, and PHP. It is also an easy language to debug, test, and maintain.Source: https://www.northeastern.edu/.../most-popular.../\", \"posted_on\": \"2022-08-30T07:54:35.802503\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid02UUbidMXFG92kTrtFn2wDtf7sYzwVr3LFMCrsFAMpyjt6FrV9jjn5m72cP1QX7ehrl&id=102394349277873&__cft__[0]=AZV7Vji1qaBJ4QgvhfWurdHsnciye-l09e3KCDGpWjz05KhmPiK3S9hAKvMuSrwFbxuOGTIqxyMvqW11plFn84SrBeFXmitPA3HaTA_iWHXXombrEqJvb4X2FNro7W6WSgheqfK_6uviwe0E2yeIvDtQuSJqDIvISGV5qB_-g-WGd7YkxoARjVXiXa5HDplZ4s1IxaWjMo2MnOLJTbyAL_k1&__tn__=%2CO%2CP-R\"}, \"pfbid0y3Y41TG3v5z1EPMPR3YGeputyXXjAtzhurBgfbduwhd86dkt6go8imccaEy7M9qol\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"Microsoft developed C# as a faster and more secure variant of C. It is fully integrated with Microsoft’s .NET software framework, which supports the development of applications for Windows, browser plug-ins, and mobile devices. C# offers shared codebases, a large code library, and a variety of data types.Source: https://www.northeastern.edu/.../most-popular.../\", \"posted_on\": \"2022-08-30T07:55:35.876437\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid0y3Y41TG3v5z1EPMPR3YGeputyXXjAtzhurBgfbduwhd86dkt6go8imccaEy7M9qol&id=102394349277873&__cft__[0]=AZUHpMOuBV-PMAr-2imo8DIj4vR-zeHG8nr3g7BnRDV5wYLG4f4giLYfclw7dwVEFKUQ5AYbFZGLIxVMJLWuI9O59DTBnQX-R_unjylSCuCpdQeqXImS7gQZUyZQ9LXZdD3D_8r1FLqvmzI228eF33Fs6o77kwMDCDYZFX2FIohhJUdxDRb5vlZ7UMpXrDkBSg6HrIdro4xs4LQ59KxFSYXi&__tn__=%2CO%2CP-R\"}, \"pfbid02qgjzYCreR8Es3o6nGTv8HUDEKjRMnqPrH8mpjBSJnQKNevYzD9ttpzYCnayKXqoql\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"Java is the programming language most commonly associated with the development of client-server applications, which are used by large businesses around the world. Java is designed to be a loosely coupled programming language, meaning that an application written in Java can run on any platform that supports Java. As a result, Java is described as the “write once, run anywhere” programming language.Source: https://www.northeastern.edu/.../most-popular.../\", \"posted_on\": \"2022-08-30T07:55:36.922781\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid02qgjzYCreR8Es3o6nGTv8HUDEKjRMnqPrH8mpjBSJnQKNevYzD9ttpzYCnayKXqoql&id=102394349277873&__cft__[0]=AZUo8IN-SEJbPh22_nO0zFgV73gDvO1UYuJagRLsbNQdeJbGK8ilXqhFVWeI5wthM-u5INpoplvwqdMnQewaVf63SIG3u173bwiwTpBIcEoRvXm10rZiNbTQ9PHlGok7RuidfKCw1PLMFlGfr7FzNohJyUU1Lylp02DSa9wWjq3YdvEZKNV6F0h-kMb0VSd8dSpXURVq1VvGPr_gw7aPuDld&__tn__=%2CO%2CP-R\"}, \"pfbid02QQACraXBLh5MnyYhoerGVJM9wup91MFa58GJFTFHPXwPaqcFMUes9MFHvcXkJ1rNl\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"JavaScript is the most popular programming language for building interactive websites; “virtually everyone is using it,” Gorton says. When combined with Node.js, programmers can use JavaScript to produce web content on the server before a page is sent to the browser, which can be used to build games and communication applications that run directly in the browser. A wide variety of add-ons extend the functionality of JavaScript as well. Source : https://www.northeastern.edu/… See more\", \"posted_on\": \"2022-08-30T07:56:36.989678\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid02QQACraXBLh5MnyYhoerGVJM9wup91MFa58GJFTFHPXwPaqcFMUes9MFHvcXkJ1rNl&id=102394349277873&__cft__[0]=AZWPj3MCQ6Z_hCZEdb0B0SiNnoBR3hrbd5RqO6O01xSAKSAf5uuVPIfTl1n4nb6S_m5-r_gILsfdO3rwsts-C4kS02JOAZGKV_urQFnWjI-sLYRPi7EG7L4YsXSntfV8NnnXsdCeWEvRz80rLYX9-Dk9q5m1JKqiZIE4d1BGhgNmSfxfLt9Gy2ZqVpjMrB9TrLD2XKpR7U2svrFE3oT0TtCW&__tn__=%2CO%2CP-R\"}, \"pfbid036XeQd558bNyXCDwgxR5kyA5RgvEvbVtXPerwAXUe6qPgD3d2cB7itMR4165xND7Bl\": {\"name\": \"Generalsoftwareengineeringposts\", \"shares\": 0, \"reactions\": {\"likes\": 0, \"loves\": 0, \"wow\": 0, \"cares\": 0, \"sad\": 0, \"angry\": 0, \"haha\": 0}, \"reaction_count\": 0, \"comments\": 0, \"content\": \"Python is widely regarded as a programming language that’s easy to learn, due to its simple syntax, a large library of standards and toolkits, and integration with other popular programming languages such as C and C++. In fact, it’s the first language that students learn in the Align program, Gorton says. “You can cover a lot of computer science concepts quickly, and it’s relatively easy to build on.” It is a popular programming language, especially among startups, and theref… See more\", \"posted_on\": \"2022-08-30T07:57:37.055368\", \"video\": \"\", \"image\": [], \"post_url\": \"https://www.facebook.com/permalink.php?story_fbid=pfbid036XeQd558bNyXCDwgxR5kyA5RgvEvbVtXPerwAXUe6qPgD3d2cB7itMR4165xND7Bl&id=102394349277873&__cft__[0]=AZV7wkPr8rUOblxejxFQYimHK9gGmP60fFcPq2TcPpCxsEUsiFEqRZF8SsvhPpBForFXBnjYcCh18HOf7bKRMk0OVSvkDTB_xICMK__-OVyWdGTKhzHnOZc2HBME8s9Wa1FuePN7Awhf70u3FsWSEOifSc3fMBVmjaNgtRNf-BFwDxoZBwQSKredCc4Jpd3sRWi2TY380WU34dg0-POk9KhB&__tn__=%2CO%2CP-R\"}}"
]
```

- Also, we created a POST HTTP method to start the scraping of a custom FB page using the following command:

```bash
curl -X POST -H "Content-type: application/json" -d "{\"page_name\" : \"Generalsoftwareengineeringposts-102394349277873\"}" "127.0.0.1:8000/custom_scraping"
```

- Then to check the scraping data stored in mongodb, you need to go to "http://127.0.0.1:8008/display_raw_documents":

```bash
{
  "pages": [
    {
      "Page": "Generalsoftwareengineeringposts-102394349277873",
      "data": {
        "pfbid02jZNYtix1Vu3ocetkE7QDQ1tZCvko5vNQ5AnirvTPvDWsv3K89yQdPQhQyYknGvXMl": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "PHP is widely used for server-side web development, when a website frequently requests information from a server. As an older language, PHP benefits from a large ecosystem of users who have produced frameworks, libraries, and automation tools to make the programming language easier to use. PHP code is also easy to debug.Source: https://www.northeastern.edu/.../most-popular.../",
          "posted_on": "2022-08-30T07:12:34.648493",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02jZNYtix1Vu3ocetkE7QDQ1tZCvko5vNQ5AnirvTPvDWsv3K89yQdPQhQyYknGvXMl&id=102394349277873&__cft__[0]=AZX7aqRfUCB4kOdXkQL2x2Dpo_FjaLZUathrdnmP6dv_qOQZi8aWJPGcYNInTTKbJ0sw-OVOqffVU3j3KIqOGInukc3VXS6blE_LislHdpQeghb9SdcF_Sjfstcnq5uGvj-SPuEbZYWyu99Y6e5CpEJ5YSAIjDTYMaq1L8g5alYf33XHCesP2N3FXpj8IMH5hP0cpZnzFd7zb2Db5e9F9ScY&__tn__=%2CO%2CP-R"
        },
        "pfbid02LotwHKt4n2UTdkxUnoxwHpbF23mQgGbYhEXAXTe9WRFWkts2ZjPkRJ4sTWxdFm1jl": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "Swift is Apple’s language for developing applications for Mac computers and Apple’s mobile devices, including the iPhone, iPad, and Apple Watch. Like many modern programming languages, Swift has a highly readable syntax, runs code quickly, and can be used for both client-side and server-side development. Source: https://www.northeastern.edu/.../most-popular.../",
          "posted_on": "2022-08-30T07:53:34.719371",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02LotwHKt4n2UTdkxUnoxwHpbF23mQgGbYhEXAXTe9WRFWkts2ZjPkRJ4sTWxdFm1jl&id=102394349277873&__cft__[0]=AZU8d4y8XphmXHt_l02mkz1kK559msfGFJEzu0gDwHXi-hQYteiR47M8PVu8n2R-Xa2GqcQ9Hxh56pBWp9nqe_mfn2PvmwSk3-lFw_KCFn3k9yay7Yw6AuZlymnyt3f95y-X0Pp-K7zTlBNQyeUMK1gN7Tia1aFcZvHBo2rVV8QF3r0QG_zEul_QqEp_7QRtIOvQ7pcld24TFIIHtYr3p9_N&__tn__=%2CO%2CP-R"
        },
        "pfbid02aX483iU2Q43fBiLtkum331NYo8rhLVinTMTxy8dVN7PXKvXZSsu8aHNXBNfVZMb3l": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "R is heavily used in statistical analytics and machine learning applications. The language is extensible and runs on many operating systems. Many large companies have adopted R in order to analyze their massive data sets, so programmers who know R are in great demand. Source: https://www.northeastern.edu/.../most-popular.../",
          "posted_on": "2022-08-30T07:53:34.786311",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02aX483iU2Q43fBiLtkum331NYo8rhLVinTMTxy8dVN7PXKvXZSsu8aHNXBNfVZMb3l&id=102394349277873&__cft__[0]=AZV647g1CMdg9wVr7Z3Dfa47chgqFxtvW8U6bSopQaB2wO9NzLMQK_uErN9ChD6J-ZMmtMLeNnSRhMKFIHCS9ouZeVE6mNEENfUIhW-mr6ygsS-O174cXhw0nHhu-nnmbc2XnqIKAmsjn7gN2XYw-Wzp3QreNV4mM_TpCxYi5jlEJjRHyrB5BPn_NcVBI64NbpM_X2-vTQ7u3s73BSH0ygve&__tn__=%2CO%2CP-R"
        },
        "pfbid02cmT97hcvsaViCdUVVQhHADqVN6UoFzWsTbvHkJc9tNMAUPzGeT2jaWUcymRCoQvXl": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "Also referred to as Golang, Go was developed by Google to be an efficient, readable, and secure language for system-level programming. It works well for distributed systems, in which systems are located on different networks and need to communicate by sending messages to each other. While it is a relatively new language, Go has a large standards library and extensive documentation.Source: https://www.northeastern.edu/.../most-popular.../",
          "posted_on": "2022-08-30T07:54:34.859120",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02cmT97hcvsaViCdUVVQhHADqVN6UoFzWsTbvHkJc9tNMAUPzGeT2jaWUcymRCoQvXl&id=102394349277873&__cft__[0]=AZWl6MOkGf1C225oZJY-vqZulO-lakdeq4H1fduXDsJB3rmy0XBwccGBtGCpJBmLDP7KHtQeH_m0pGbpEeXekJ3hdQtb6QQjZ_G3k-pEPIe9xih9uwUl_B1IPmhvGqC-IJrucdJWACXRIiEkhXJ1rgWyfN1vhlw902ulY6r2R4v2juASvKDjHYhyePsE0heqLDrH_jDxj5qMwYK1KVAnIYfE&__tn__=%2CO%2CP-R"
        },
        "pfbid0mcJYEekjvo64k52uXNwgWpmnqjwuwL5waXtDyXEap6g2d6gcPzgSTULPd7WGELF8l": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "C++ is an extension of C that works well for programming the systems that run applications, as opposed to the applications themselves. C++ also works well for multi-device and multi-platform systems. Over time, programmers have written a large set of libraries and compilers for C++. Being able to use these utilities effectively is just as important to understanding a programming language as writing code, Gorton says.Source: https://www.northeastern.edu/.../most-popular.../… See more",
          "posted_on": "2022-08-30T07:54:35.733397",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid0mcJYEekjvo64k52uXNwgWpmnqjwuwL5waXtDyXEap6g2d6gcPzgSTULPd7WGELF8l&id=102394349277873&__cft__[0]=AZVnUPbi4Zs_aNmgq7QenAvAYunm-atDDlowPdf6yNj1OXcJigFOEl2niTLvrfu7fBH574vFFbThpxgLcUNinvj9VEv_qYw7MtdMPzNrp1U966iFRkou45J3C7B3KCSkx-Yd5uLibElLYY10x6vQyKK2sB9x7dXJbT7Wz57kVgTayuQxkTZbTva4HUH0oK3inFHMGT1xGM0ppu9lbL51z6Ia&__tn__=%2CO%2CP-R"
        },
        "pfbid02UUbidMXFG92kTrtFn2wDtf7sYzwVr3LFMCrsFAMpyjt6FrV9jjn5m72cP1QX7ehrl": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "Along with Python and Java, C forms a “good foundation” for learning how to program, Gorton says. As one of the first programming languages ever developed, C has served as the foundation for writing more modern languages such as Python, Ruby, and PHP. It is also an easy language to debug, test, and maintain.Source: https://www.northeastern.edu/.../most-popular.../",
          "posted_on": "2022-08-30T07:54:35.802503",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02UUbidMXFG92kTrtFn2wDtf7sYzwVr3LFMCrsFAMpyjt6FrV9jjn5m72cP1QX7ehrl&id=102394349277873&__cft__[0]=AZV7Vji1qaBJ4QgvhfWurdHsnciye-l09e3KCDGpWjz05KhmPiK3S9hAKvMuSrwFbxuOGTIqxyMvqW11plFn84SrBeFXmitPA3HaTA_iWHXXombrEqJvb4X2FNro7W6WSgheqfK_6uviwe0E2yeIvDtQuSJqDIvISGV5qB_-g-WGd7YkxoARjVXiXa5HDplZ4s1IxaWjMo2MnOLJTbyAL_k1&__tn__=%2CO%2CP-R"
        },
        "pfbid0y3Y41TG3v5z1EPMPR3YGeputyXXjAtzhurBgfbduwhd86dkt6go8imccaEy7M9qol": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "Microsoft developed C# as a faster and more secure variant of C. It is fully integrated with Microsoft’s .NET software framework, which supports the development of applications for Windows, browser plug-ins, and mobile devices. C# offers shared codebases, a large code library, and a variety of data types.Source: https://www.northeastern.edu/.../most-popular.../",
          "posted_on": "2022-08-30T07:55:35.876437",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid0y3Y41TG3v5z1EPMPR3YGeputyXXjAtzhurBgfbduwhd86dkt6go8imccaEy7M9qol&id=102394349277873&__cft__[0]=AZUHpMOuBV-PMAr-2imo8DIj4vR-zeHG8nr3g7BnRDV5wYLG4f4giLYfclw7dwVEFKUQ5AYbFZGLIxVMJLWuI9O59DTBnQX-R_unjylSCuCpdQeqXImS7gQZUyZQ9LXZdD3D_8r1FLqvmzI228eF33Fs6o77kwMDCDYZFX2FIohhJUdxDRb5vlZ7UMpXrDkBSg6HrIdro4xs4LQ59KxFSYXi&__tn__=%2CO%2CP-R"
        },
        "pfbid02qgjzYCreR8Es3o6nGTv8HUDEKjRMnqPrH8mpjBSJnQKNevYzD9ttpzYCnayKXqoql": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "Java is the programming language most commonly associated with the development of client-server applications, which are used by large businesses around the world. Java is designed to be a loosely coupled programming language, meaning that an application written in Java can run on any platform that supports Java. As a result, Java is described as the “write once, run anywhere” programming language.Source: https://www.northeastern.edu/.../most-popular.../",
          "posted_on": "2022-08-30T07:55:36.922781",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02qgjzYCreR8Es3o6nGTv8HUDEKjRMnqPrH8mpjBSJnQKNevYzD9ttpzYCnayKXqoql&id=102394349277873&__cft__[0]=AZUo8IN-SEJbPh22_nO0zFgV73gDvO1UYuJagRLsbNQdeJbGK8ilXqhFVWeI5wthM-u5INpoplvwqdMnQewaVf63SIG3u173bwiwTpBIcEoRvXm10rZiNbTQ9PHlGok7RuidfKCw1PLMFlGfr7FzNohJyUU1Lylp02DSa9wWjq3YdvEZKNV6F0h-kMb0VSd8dSpXURVq1VvGPr_gw7aPuDld&__tn__=%2CO%2CP-R"
        },
        "pfbid02QQACraXBLh5MnyYhoerGVJM9wup91MFa58GJFTFHPXwPaqcFMUes9MFHvcXkJ1rNl": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "JavaScript is the most popular programming language for building interactive websites; “virtually everyone is using it,” Gorton says. When combined with Node.js, programmers can use JavaScript to produce web content on the server before a page is sent to the browser, which can be used to build games and communication applications that run directly in the browser. A wide variety of add-ons extend the functionality of JavaScript as well. Source : https://www.northeastern.edu/… See more",
          "posted_on": "2022-08-30T07:56:36.989678",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid02QQACraXBLh5MnyYhoerGVJM9wup91MFa58GJFTFHPXwPaqcFMUes9MFHvcXkJ1rNl&id=102394349277873&__cft__[0]=AZWPj3MCQ6Z_hCZEdb0B0SiNnoBR3hrbd5RqO6O01xSAKSAf5uuVPIfTl1n4nb6S_m5-r_gILsfdO3rwsts-C4kS02JOAZGKV_urQFnWjI-sLYRPi7EG7L4YsXSntfV8NnnXsdCeWEvRz80rLYX9-Dk9q5m1JKqiZIE4d1BGhgNmSfxfLt9Gy2ZqVpjMrB9TrLD2XKpR7U2svrFE3oT0TtCW&__tn__=%2CO%2CP-R"
        },
        "pfbid036XeQd558bNyXCDwgxR5kyA5RgvEvbVtXPerwAXUe6qPgD3d2cB7itMR4165xND7Bl": {
          "name": "Generalsoftwareengineeringposts",
          "shares": 0,
          "reactions": {
            "likes": 0,
            "loves": 0,
            "wow": 0,
            "cares": 0,
            "sad": 0,
            "angry": 0,
            "haha": 0
          },
          "reaction_count": 0,
          "comments": 0,
          "content": "Python is widely regarded as a programming language that’s easy to learn, due to its simple syntax, a large library of standards and toolkits, and integration with other popular programming languages such as C and C++. In fact, it’s the first language that students learn in the Align program, Gorton says. “You can cover a lot of computer science concepts quickly, and it’s relatively easy to build on.” It is a popular programming language, especially among startups, and theref… See more",
          "posted_on": "2022-08-30T07:57:37.055368",
          "video": "",
          "image": [
            
          ],
          "post_url": "https://www.facebook.com/permalink.php?story_fbid=pfbid036XeQd558bNyXCDwgxR5kyA5RgvEvbVtXPerwAXUe6qPgD3d2cB7itMR4165xND7Bl&id=102394349277873&__cft__[0]=AZV7wkPr8rUOblxejxFQYimHK9gGmP60fFcPq2TcPpCxsEUsiFEqRZF8SsvhPpBForFXBnjYcCh18HOf7bKRMk0OVSvkDTB_xICMK__-OVyWdGTKhzHnOZc2HBME8s9Wa1FuePN7Awhf70u3FsWSEOifSc3fMBVmjaNgtRNf-BFwDxoZBwQSKredCc4Jpd3sRWi2TY380WU34dg0-POk9KhB&__tn__=%2CO%2CP-R"
        }
      }
    }
  ]
}
```


- And to check the scraping data posts stored in mongodb, you need to go to "http://127.0.0.1:8008/display_raw_documents":

```bash
{
  "pages": [
    {
      "Page": "Generalsoftwareengineeringposts-102394349277873",
      "Posts": [
        {
          "Post id": "pfbid02jZNYtix1Vu3ocetkE7QDQ1tZCvko5vNQ5AnirvTPvDWsv3K89yQdPQhQyYknGvXMl",
          "Content": "PHP is widely used for server-side web development, when a website frequently requests information from a server. As an older language, PHP benefits from a large ecosystem of users who have produced frameworks, libraries, and automation tools to make the programming language easier to use. PHP code is also easy to debug.Source: https://www.northeastern.edu/.../most-popular.../"
        },
        {
          "Post id": "pfbid02LotwHKt4n2UTdkxUnoxwHpbF23mQgGbYhEXAXTe9WRFWkts2ZjPkRJ4sTWxdFm1jl",
          "Content": "Swift is Apple’s language for developing applications for Mac computers and Apple’s mobile devices, including the iPhone, iPad, and Apple Watch. Like many modern programming languages, Swift has a highly readable syntax, runs code quickly, and can be used for both client-side and server-side development. Source: https://www.northeastern.edu/.../most-popular.../"
        },
        {
          "Post id": "pfbid02aX483iU2Q43fBiLtkum331NYo8rhLVinTMTxy8dVN7PXKvXZSsu8aHNXBNfVZMb3l",
          "Content": "R is heavily used in statistical analytics and machine learning applications. The language is extensible and runs on many operating systems. Many large companies have adopted R in order to analyze their massive data sets, so programmers who know R are in great demand. Source: https://www.northeastern.edu/.../most-popular.../"
        },
        {
          "Post id": "pfbid02cmT97hcvsaViCdUVVQhHADqVN6UoFzWsTbvHkJc9tNMAUPzGeT2jaWUcymRCoQvXl",
          "Content": "Also referred to as Golang, Go was developed by Google to be an efficient, readable, and secure language for system-level programming. It works well for distributed systems, in which systems are located on different networks and need to communicate by sending messages to each other. While it is a relatively new language, Go has a large standards library and extensive documentation.Source: https://www.northeastern.edu/.../most-popular.../"
        },
        {
          "Post id": "pfbid0mcJYEekjvo64k52uXNwgWpmnqjwuwL5waXtDyXEap6g2d6gcPzgSTULPd7WGELF8l",
          "Content": "C++ is an extension of C that works well for programming the systems that run applications, as opposed to the applications themselves. C++ also works well for multi-device and multi-platform systems. Over time, programmers have written a large set of libraries and compilers for C++. Being able to use these utilities effectively is just as important to understanding a programming language as writing code, Gorton says.Source: https://www.northeastern.edu/.../most-popular.../… See more"
        },
        {
          "Post id": "pfbid02UUbidMXFG92kTrtFn2wDtf7sYzwVr3LFMCrsFAMpyjt6FrV9jjn5m72cP1QX7ehrl",
          "Content": "Along with Python and Java, C forms a “good foundation” for learning how to program, Gorton says. As one of the first programming languages ever developed, C has served as the foundation for writing more modern languages such as Python, Ruby, and PHP. It is also an easy language to debug, test, and maintain.Source: https://www.northeastern.edu/.../most-popular.../"
        },
        {
          "Post id": "pfbid0y3Y41TG3v5z1EPMPR3YGeputyXXjAtzhurBgfbduwhd86dkt6go8imccaEy7M9qol",
          "Content": "Microsoft developed C# as a faster and more secure variant of C. It is fully integrated with Microsoft’s .NET software framework, which supports the development of applications for Windows, browser plug-ins, and mobile devices. C# offers shared codebases, a large code library, and a variety of data types.Source: https://www.northeastern.edu/.../most-popular.../"
        },
        {
          "Post id": "pfbid02qgjzYCreR8Es3o6nGTv8HUDEKjRMnqPrH8mpjBSJnQKNevYzD9ttpzYCnayKXqoql",
          "Content": "Java is the programming language most commonly associated with the development of client-server applications, which are used by large businesses around the world. Java is designed to be a loosely coupled programming language, meaning that an application written in Java can run on any platform that supports Java. As a result, Java is described as the “write once, run anywhere” programming language.Source: https://www.northeastern.edu/.../most-popular.../"
        },
        {
          "Post id": "pfbid02QQACraXBLh5MnyYhoerGVJM9wup91MFa58GJFTFHPXwPaqcFMUes9MFHvcXkJ1rNl",
          "Content": "JavaScript is the most popular programming language for building interactive websites; “virtually everyone is using it,” Gorton says. When combined with Node.js, programmers can use JavaScript to produce web content on the server before a page is sent to the browser, which can be used to build games and communication applications that run directly in the browser. A wide variety of add-ons extend the functionality of JavaScript as well. Source : https://www.northeastern.edu/… See more"
        },
        {
          "Post id": "pfbid036XeQd558bNyXCDwgxR5kyA5RgvEvbVtXPerwAXUe6qPgD3d2cB7itMR4165xND7Bl",
          "Content": "Python is widely regarded as a programming language that’s easy to learn, due to its simple syntax, a large library of standards and toolkits, and integration with other popular programming languages such as C and C++. In fact, it’s the first language that students learn in the Align program, Gorton says. “You can cover a lot of computer science concepts quickly, and it’s relatively easy to build on.” It is a popular programming language, especially among startups, and theref… See more"
        }
      ]
    }
  ]
}
```


## Test 

To test the APIs, we used pytest python library. we created some unit tests in "test_app.py".

We can confirm locally that the tests pass by running:
```bash
python -m pytest
```

But, We'd like to run those unit tests on every pull request such that we don't accidentally introduce code that breaks them.

To set that up, we are going to use GitHub Actions by creating a file in our repository over at .github/workflows/unit-tests.yml.

So, in the previous file, we checked the code style using flake8 and python tests.


## Contributing
The main branch contain the last tested version.

Pull requests are welcome. 

Please make sure to create a new branch and push new changes there.

