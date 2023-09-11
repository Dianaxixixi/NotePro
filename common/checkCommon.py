import unittest


class CheckTools(unittest.TestCase):
    def check_output(self, expect, actual):
        """
        :expect:{responseTime:int,contentVersion:int,infoUpdateTime:int}
        :actual:response.json()

        校验点：
        1.必填项是否存在
        2.返回字段的类型是否一致
        3.没有呢多余的字段出现

        ;:return: None
        """
        self.assertEqual(len(expect.keys()), len(actual.keys()), msg='字段长度不匹配')  # 校验字段长度是否一致
        for k, v in expect.items():  # 实际接口返回结果里面值的类型是是字典里面嵌套了字典的情况
            if type(v) == dict:  # 遇到嵌套的字典，进行递归  实际接口返回结果里面值的类型是是字典里面嵌套了字典的情况
                # eg: actual_output = {'infoVersion': 1, 'webNotes': {'noteId': '001', 'createTime': 1233}}
                self.check_output(expect[k], actual[k])  # 递归 返回结果遇到嵌套的字段进行递归
            elif type(v) == list:  # 实际接口返回结果里面值的类型是是列表
                for item in range(len(expect[k])):   # 遍历列表中所有的元素
                    if type(expect[k][item]) == dict:  # 如果接口返回是列表中嵌套包含字典
                        self.check_output(expect[k][item], actual[k][item])
                    else:
                        if type(expect[k][item]) == type:
                            self.assertEqual(expect[k][item], type(actual[k][item]), msg=f'{k} 字段类型不一致')  # 校验类型
                        else:
                            self.assertEqual(type(expect[k][item]), type(actual[k][item]), msg=f'{k} 字段类型不一致')  # 校验类型
                            self.assertEqual(expect[k][item], actual[k][item], msg=f'{k} 字段值不一致')  # 校验类型
            else:
                self.assertIn(k, actual.keys(), msg=f'{k} 字段不存在')  # 校验字段是否存在
                if type(v) == type:
                    self.assertEqual(v, type(actual[k]), msg=f'{k} 字段类型不一致')  # 校验类型
                else:
                    self.assertEqual(type(v), type(actual[k]), msg=f'{k} 字段类型不一致')  # 校验类型
                    self.assertEqual(v, actual[k], msg=f'{k} 字段值不一致')

