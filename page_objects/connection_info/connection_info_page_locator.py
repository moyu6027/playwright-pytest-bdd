class ConnInfoPageLocator:
    CONN_INFO_URL = "/admin/connectInfo"
    # ADD = "(//button[@class='next-btn next-medium next-btn-primary'])[1]"
    ADD = "'添加'"
    DISCOVER_CONN = "//em[@title='发现采集']"
    SNMP_TYPE = "//em[@title='SNMP']"
    NAME = '//label[contains(text(),"名称")]/../..//input[@placeholder="请输入"]'
    PORT = "(//input[@placeholder='请输入'])[2]"
    READ_ONLY = "(//input[@placeholder='请输入'])[3]"
    V2C = "//em[@title='v2c']"
    SAVE = "//span[text()='保存']"
    CONFIRM = "//span[text()='确定']"
