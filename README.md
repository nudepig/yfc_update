### 继承的方式修改了部分模型方式和视图
1.修改了网站商城的显示方式，使其登录可见
2.扩展了res.partner字段，新增了pricelist_id字段，此字段关联了价格表
3.修改了wbsite_sale的视图，使得网站商城按照用户的pricelist_id显示对应的价格表
4.在sale.order新增加了方法，是的销售员绑定销售团队
5.修改了sale_views视图，使得客户、产品、销售员、销售团队选择框不能创建