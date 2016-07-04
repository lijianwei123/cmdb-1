#JumpServer CMDB API 

### 1. Asset API
##### 1. asset add
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/add    | POST	 		 | 200   |
		
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| hostname      | 是	 		 | String   |主机名  |server01|
	| ip            | 否|String|ip地址|192.168.1.1|
	|other_ip|否|String|其他ip|[10.0.0.1, 10.0.0.2]
	|port|否|int|主机端口|22|
	|group|否||主机组|[数据库，DBA]|
	|idc|否|String|IDC机房|chinanet|
	|mac|否|String|mac地址|ac:bc:32:82:88:ad|
	|cpu|否|String|主机cpu|E2690*24|
	|memory|否|String|主机memory|64G|
	|disk|否|String|主机disk|{"sda":500G,"sdb":1T}|
	|sn|否|String|主机sn号|TX98GN|
	|number|否|String|主机资产编号|ABC-0001|
	|cabinet|否|String|机柜号|2-9|
	|postion|否|int|主机所在机柜位置|2|
	|system_type|否|String|系统类型|CentOS|
	|device_type|否|String|设备类型|物理机|
	|env|否|String|环境|线上|
	|status|否|String|状态|已使用|
	|brand|否|String|品牌|Dell|
	|system_version|否|String|系统版本号|6.6|
	|tags|否|String|标签|[数据库, 主站]
	|is_active|否|String|是否激活|是|
	|comment|否|String|备注|数据库服务器master|
	
	
* Example 
	
	post url: /asset/add
	
	parameter: 
		
		{
			"hostname": "server01", 
			"ip": "192.168.1.1", 
			"port": 22, 
			"idc": "chinanet",
 			"sn": "TX98GN"
		}
		
	return:
		
		{
			"code": 200,
			"message": "success"
		}	
	
##### 2. asset edit
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/edit   | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| hostname      | 是	 		 | String   |主机名  |server01|
	| ip            | 否|String|ip地址|192.168.1.1|
	|other_ip|否|String|其他ip|[10.0.0.1, 10.0.0.2]
	|port|否|int|主机端口|22|
	|group|否||主机组|[数据库，DBA]|
	|idc|否|String|IDC机房|chinanet|
	|mac|否|String|mac地址|ac:bc:32:82:88:ad|
	|cpu|否|String|主机cpu|E2690*24|
	|memory|否|String|主机memory|64G|
	|disk|否|String|主机disk|{"sda":500G,"sdb":1T}|
	|sn|否|String|主机sn号|TX98GN|
	|number|否|String|主机资产编号|ABC-0001|
	|cabinet|否|String|机柜号|2-9|
	|postion|否|int|主机所在机柜位置|2|
	|system_type|否|String|系统类型|CentOS|
	|device_type|否|String|设备类型|物理机|
	|env|否|String|环境|线上|
	|status|否|String|状态|已使用|
	|brand|否|String|品牌|Dell|
	|system_version|否|String|系统版本号|6.6|
	|tags|否|String|标签|[数据库, 主站]
	|is_active|否|String|是否激活|是|
	|comment|否|String|备注|数据库服务器master|
	
	
##### 3. asset del
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/del    | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| hostname      | 是	 		 | String|主机名  |
	
	
	
##### 4. asset detail
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/detail | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| hostname      | 是	 		 | String|主机名  |
	
		
	
	
##### 5. asset list
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/list    | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| hostname      | 是	 		 | String|主机名  |

		
	
	
	



### 2. AssetGroup API
##### 1. asset group add

* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/group/add    | POST	 		 | 200   |
		
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| name      | 是	 		 | String   |主机名  |group01|
	| tags            | 否|String|标签|[重要, 研发]|
	| user_add            | 否|String|创建人|李刚|
	| comment           | 否|String|备注|group01|
	
	
	
* Example 
	
	post url: /asset/group/add
	
	parameter: 
		
		{
			"name": "group01", 
			"tags": ["重要", "研发"], 
			"user_add": "李刚",
			"comment": "group01"
		}
		
	return:
		
		{
			"code": 200,
			"message": "success"
		}	
	
##### 2. asset group edit
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/group/edit   | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| name      | 是	 		 | String   |主机名  |group01|
	| tags            | 否|String|标签|[重要, 研发]|
	| user_add            | 否|String|创建人|李刚|
	| comment           | 否|String|备注|group01|
	
	
	
* Example 
	
	post url: /asset/group/edit
	
	parameter: 
		
		{
			"name": "group01", 
			"tags": ["重要", "研发"], 
			"user_add": "李刚",
			"comment": "group01"
		}
		
	return:
		
		{
			"code": 200,
			"message": "success"
		}	

	
	
##### 3. asset group del
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/group/del    | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|主机组名|
	
	
	
##### 4. asset group detail
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/group/detail | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|主机组名|
	
		
	
	
##### 5. asset group list
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/group/list    | GET	 | 200   | 
	
	

### 3. IDC API
##### 1. idc add

* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/idc/add    | POST	 		 | 200   |
		
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| name      | 是	 		 | String   |IDC名  |chinanet|
	| linkman            | 否|String|标签|李刚|
	| phone            | 否|String|电话|18888888888|
	| address          | 否|String|地址|北京市天安门路一号|
	| network            | 否|String|网络|["192.168.1.0/24", "172.16.1.0/16"]|
	| assets            | 否|String|包含主机|["server01", "server02", "server03"]|
	| comment           | 否|String|备注|BGP核心机房|
	
	
	
* Example 
	
	post url: /asset/idc/add
	
	parameter: 
		
    {
        "name": "chinanet",
        "linkman", "李刚",
        "phone": "18888888888",
        "address": "北京市天安门路一号",
        "network": ["192.168.1.0/24", "172.16.1.0/16"],
        "assets": ["server01", "server02", "server03"],
        "comment": "BGP核心机房"
    }
		
	return:
		
		{
			"code": 200,
			"message": "success"
		}	
	
##### 2. idc edit
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/idc/edit    | POST	 		 | 200   |
		
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| name      | 是	 		 | String   |IDC名  |chinanet|
	| linkman            | 否|String|标签|李刚|
	| phone            | 否|String|电话|18888888888|
	| address          | 否|String|地址|北京市天安门路一号|
	| network            | 否|String|网络|["192.168.1.0/24", "172.16.1.0/16"]|
	| assets            | 否|String|包含主机|["server01", "server02", "server03"]|
	| comment           | 否|String|备注|BGP核心机房|
	
	
	
* Example 
	
	post url: /asset/idc/edit
	
	parameter: 
		
		{
			"name": "chinanet", 
			"linkman", "李刚", 
			"phone": "18888888888",
			"address": "北京市天安门路一号",
			"network": ["192.168.1.0/24", "172.16.1.0/16"],
			"assets": ["server01", "server02", "server03"],
			"comment": "BGP核心机房"
		}
		
	return:
		
		{
			"code": 200,
			"message": "success"
		}	
	

	
	
##### 3. idc del
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/idc/del    | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|idc名|
	
	
	
##### 4. idc detail
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/idc/detail | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|idc名|
	
		
	
	
##### 5. idc list
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/idc/list    | GET 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|idc名|
	
	
### 3. Tag API
##### 1. tag add

* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/tag/add    | POST	 		 | 200   |
		
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| key      | 是	 		 | String   |key名称  |系统类型|
	| value            | 是|String|value值|Windows|
	| user_add            | 是|String|添加人|李刚|
	| comment           | 否|String|备注|系统类型标签|
	
	
	
* Example 
	
	post url: /asset/tag/add
	
	parameter: 
		
		{
			"key": "系统类型",
			"value": "Windows",
			"user_add": "李刚",
			"comment": "系统类型标签" 
		}
		
	return:
		
		{
			"code": 200,
			"message": "success"
		}	
	
##### 2. tag edit

* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/tag/edit    | POST	 		 | 200   |
		
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |示例|
	| ------------- |:-------------:| -----:|---- :|---- :|
	| key      | 是	 		 | String   |key名称  |系统类型|
	| value            | 是|String|value值|Windows|
	| user_add            | 是|String|添加人|李刚|
	| comment           | 否|String|备注|系统类型标签|
	
	
	
* Example 
	
	post url: /asset/tag/edit
	
	parameter: 
		
		{
			"key": "系统类型",
			"value": "Windows",
			"user_add": "李刚",
			"comment": "系统类型标签" 
		}
		
	return:
		
		{
			"code": 200,
			"message": "success"
		}	

	
	
##### 3. tag del
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/tag/del    | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|idc名|
	
	
	
##### 4. tag detail
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/tag/detail | POST	 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|idc名|
	
		
	
	
##### 5. tag list
* URL/Method/CODE

	| URL           | method        | code  |
	| ------------- |:-------------:| -----:|
	| /asset/tag/list    | GET 		 | 200   | 	
	
* Parameter

	| 参数     		 | 必填        	 | 类型   |描述  |
	| ------------- |:-------------:| -----:|---- :|
	| name          | 是	 		 | String|idc名|	
		
	

### 3. System user API
####1.System user add
    POST: /system_user/add
    {
        "name":“xxx",
        "username":"admin",
        "login_type":"T/S/R",  #T telnet  S ssh R rdp
        "auth_type":"L/K/M",  # L ldap K key M
        "password":"********",
        "key_content":""              ＃密钥内容，可以不用提交
        "level":0/1                 #0为普通用户，1位管理用户
        "comment":                 #备注
        "sudo_group":        #用户组 可不提交
        "shell":          #用户shell，可不提交
        "home":        ＃ 用户家目录，可不提交    "groups"        ＃ 用户，可不提交     "UID"            ＃UID，可不提交
    }
    {
     	 "success":"true/false",//返回成功与否
     	"message":""//返回信息
    }

####2.System user edit
    POST: /system_user/edit
    {
      "id":1231231
        "name":“xxx",
        "username":"admin",
        "login_type":"T/S/R",  #T telnet  S ssh R rdp
        "auth_type":"L/K/M",  # L ldap K key M
        "password":"********",
        "key_content":""              ＃密钥内容，可以不用提交
        "level":0/1                 #0为普通用户，1位管理用户
        "comment":                 #备注
        "sudo_group":        #用户组 可不提交
        "shell":          #用户shell，可不提交
        "home":        ＃ 用户家目录，可不提交    "groups"        ＃ 用户，可不提交     "UID"            ＃UID，可不提交
    }
    结果返回
    {
     	 "success":"true/false",//返回成功与否
     	"message":""//返回信息
    }

####3.System user del
    POST: /system_user/del
    {
        id:123124
    }
    {
     	 "success":"true/false",//返回成功与否
     	"message":""//返回信息
    }

####4.System user push_history
    POST: /system_user/get_push_history
    {
        id:123124
    }
    {
     	 "success":"true/false",//返回成功与否
     	"message":{
         	"tag":""
         	"asset_group":""
         	"status":0/1／2      // 0失败，1执行中，2完成
         	"push_date":“2016-07-04 21:32:00”
         	"comment":""
     	}
    }

####5.System user push_detail
    POST: /system_user/get_push_detail
    {
        id:123124
    }
    {
        "success":"true/false",//返回成功与否
     	"message":[{
         	"asset":""
         	"status":0/1／2      // 0失败，1执行中，2完成
         	"push_date":“2016-07-04 21:32:00”
         	"comment":""
     	} ,
            {}
     	]
    }



	


