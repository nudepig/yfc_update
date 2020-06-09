### 继承的方式修改了部分模型方式和视图
1. 修改了网站商城的显示方式，使其登录可见
2. 扩展了res.partner字段，新增了pricelist_id字段，此字段关联了价格表
3. 修改了wbsite_sale的视图，使得网站商城按照用户的pricelist_id显示对应的价格表
4. 在sale.order新增加了onchange方法，销售员绑定销售团队
5. 修改了sale_views视图，使得客户、产品、销售员、销售团队选择框不能创建
6. 修改了account_view视图，增加了销售团队字段，使得多对一字段没有创建的选项
7, 修改了purchase_view视图，使得多对一字段没有创建的选项