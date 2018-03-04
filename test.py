import re

str = '2323414fdfd and dfgeggfdggdf or fgfdgdfgfgsgsgdsf - 2dsgffdgfdgd  sadadad ( gerdgd'
result = re.findall(r'.{2,10}and.{2,10}|.{2,10}or.{2,10}|.{2,10}-.{2,10}|.{2,10} \( .{2,10}|.{2,10} \) .{2,10}|.{2,10} , .{2,10}',str)
print(result)