## 地址: ``

- 登陆
 pata: `/user/login`
 param:
 ```json
{"name": "haha", "pswd": "123"}
```
return: 
```json
{
  "data": {
    "user_real": "\\u725b\\u903c",  //实名
    "user_pass": "123",
    "user_role": "\\u6e38\\u5ba2", //角色
    "user_name": "haha",
    "user_phone": "12345678",
    "user_addr": "\\u4e2d\\u5357\\u6d77"
  },
  "status": true,
  "msg": ""
}
```

- 注册
  path: `/user/regist`
  param: 
  ```json
  {"user_phone": "12345678", "user_real": "\\u725b\\u903c", "user_addr": "\\u4e2d\\u5357\\u6d77", "user_pass": "123", "user_role": "\\u6e38\\u5ba2", "user_name": "haha"}
    ```
- 发布信息
    path: `/user/addNews`
    param: 
    ```json
    {"user_id": "1", "news_content": "\\u8fd9\\u662f\\u5185\\u5bb9", "news_title": "\\u8fd9\\u662f\\u6807\\u9898"}
    ```
    
- 删除信息

    path: `/user/delNews`
    param: 
    ```json
    {"news_id":1}
    ```
- 更新信息
  
  path: `/user/upNews`
  param: 
  ```json
    {"news_id": 2, "news_dt": "2014-04-21 18:23:12", "news_title": "ipdata"}
    ```
    
- 信息列表
  path: '/user/newsList'  
  param: 
  ```json
      {"page_size": 2, "current_page":1}
  ```
  return:
  ```json
    {
      "status": true,
      "data": {
        "news": [
          {
            "news_dt": "2018-05-14T07:00:54.264Z",
            "id": 2,
            "news_title": "ipdata"
          }
        ],
        "all_page": 1,
        "current_page": 1
      },
      "msg": ""
    }
    ```
- 信息详情
  path: `/user/newsDetail`
  
  param: 
  ```json
    {"news_id":2}
  ```
   return 
   ```json
        {
      "data": {
        "title": "ipdata",
        "content": "\\u8fd9\\u662f\\u5185\\u5bb9",
        "date": "2018-05-14T07:00:54.264Z"
      },
      "status": true,
      "msg": ""
    }
    ```