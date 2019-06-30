import re
from framework_data import languages
string = """Basic Operations example using TensorFlow library.\nAuthor: Aymeric Damien\nProject: https://github.com/aymericdamien/TensorFlow-Examples/\n\n\nfrom __future__ import print_function\n\nimport tensorflow as tf\n\n# Basic constant operations\n# The value returned by the constructor represents the output\n# of the Constant op.\na = tf.constant(2)\nb = tf.constant(3)\n\n# Launch the default graph.\nwith tf.Session() as sess:\n    print("a=2, b=3")\n    print("Addition with constants: %i" % sess.run(a+b))\n    print("Multiplication with constants: %i" % sess.run(a*b))\n\n# Basic Operations with variable as graph input\n# The value returned by the constructor represents the output\n# of the Variable op. (define as input when running session)\n# tf Graph input\na = tf.placeholder(tf.int16)\nb = tf.placeholder(tf.int16)\n# Define some operations\nadd = tf.add(a, b)\nmul = tf.multiply(a, b)\n\n# Launch the default graph.\nwith tf.Session() as sess:\n    # Run every operation with variable input\n    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))\n    print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))\n\n\n# ----------------\n# More in details:\n# Matrix Multiplication from TensorFlow official tutorial\n\n# Create a Constant op that produces a 1x2 matrix.  The op is\n# added as a node to the default graph.\n#\n# The value returned by the constructor represents the output\n# of the Constant op.\nmatrix1 = tf.constant([[3., 3.]])\n\n# Create another Constant that produces a 2x1 matrix.\nmatrix2 = tf.constant([[2.],[2.]])\n\n# Create a Matmul op that takes 'matrix1' and 'matrix2' as inputs.\n# The returned value, 'product', represents the result of the matrix\n# multiplication.\nproduct = tf.matmul(matrix1, matrix2)\n\n# To run the matmul op we call the session 'run()' method, passing 'product'\n# which represents the output of the matmul op.  This indicates to the call\n# that we want to get the output of the matmul op back.\n#\n# All inputs needed by the op are run automatically by the session.  They\n# typically are run in parallel.\n#\n# The call 'run(product)' thus causes the execution of threes ops in the\n# graph: the two constants and matmul.\n#\n# The output of the op is returned in 'result' as a numpy `ndarray` object.\nwith tf.Session() as sess:\nresult = sess.run(product)\nprint(result)\n# ==> [[ 12.]]"\n"""
string_2="""import random\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport numpy as np\nlist=[]\nlist1=[]\nfor i in range(200):\n    list.append([])\n    for j in range(10):\n        list[i].append(random.randint(1,5))\n\nfor i in range(200):\n    list1.append([])\n\n\nfor i in range(200):\n    sum = 0\n    for j in range(0,3):\n        sum += list[i][j]\n    list1[i].append(round(sum/3))\n\n    sum = 0\n    for j in range(3, 5):\n        sum += list[i][j]\n    list1[i].append(round(sum/2))\n\n    sum = 0\n    for j in range(5, 8):\n        sum += list[i][j]\n    list1[i].append(round(sum/3))\n\n    sum = 0\n    for j in range(8, 10):\n        sum += list[i][j]\n    list1[i].append(round(sum/2))\nprint()\nmodule1 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]\nmodule2 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]\nmodule3 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]\nmodule4 = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]\n\nfor i in range(200):\n    for j in range(1):\n        for s in module1:\n            if s[0] == list1[i][j]:\n                s[1]+=1\n    for j in range(1,2):\n        for s in module2:\n            if s[0] == list1[i][j]:\n                s[1]+=1\n    for j in range(2, 3):\n        for s in module3:\n            if s[0] == list1[i][j]:\n                s[1]+=1\n    for j in range(3, 4):\n        for s in module4:\n            if s[0] == list1[i][j]:\n                s[1]+=1\n\nmodule1= pd.DataFrame(module1, columns=['Mark', 'Количество оценок'])\nmodule1['Модуль']='1'\nmodule2= pd.DataFrame(module2, columns=['Mark', 'Количество оценок'])\nmodule2['Модуль']='2'\nmodule3= pd.DataFrame(module3, columns=['Mark', 'Количество оценок'])\nmodule3['Модуль']='3'\nmodule4= pd.DataFrame(module4, columns=['Mark', 'Количество оценок'])\nmodule4['Модуль']='4'\ndf=pd.concat([module1,module2,module3,module4])\nprint(df)\nfig, ax = plt.subplots()\n\n\ng = sns.barplot(data=df, x='Модуль', y='Количество оценок',\n                hue='Mark', ci=None)\nplt.yticks(np.arange(0, 125, step=10))\nplt.ylim(top=125)\nplt.gca().invert_xaxis()\nax.set_xbound(-1)\nax.grid(color='black', linestyle='-', linewidth=0.25, axis='y')\nax.legend(["5", "4", '3', '2', '1'], title='Оценка',\n          loc='upper left')\nplt.tight_layout()\nfig.savefig('people.png')\nplt.show()\n"""
print(string)


def framework_detector(string):
    for i in languages:
        for j in languages[i]:
            languages[i][j]['counter'] = 0
            languages[i][j]['methods'] = []

    string1 = string.split('\n')
    print("_________________________________")
    for j, i in enumerate(string1):
        if not re.match(r'#', i):  # Если эта строка НЕ комментарий
            if re.match(r'from', i):  # Если строка начинается с from
                tmp = i.split()
                for f in languages['python']:
                    for s in languages['python'][f]['lib']:
                        if re.match(s, tmp[1]):
                            languages['python'][f]['counter'] += 1
                            if tmp[2] == 'import':
                                pos = re.search(r' as ', ''.join(tmp[3:]))
                                if pos is not None:
                                    languages['python'][f]['methods'].extend(tmp[(len(tmp)-4)/2*-1:])
                                elif pos is None:
                                    languages['python'][f]['methods'].extend(tmp[3:])

            elif not re.match(r'from', i):  # Если строка не начинается с from
                if re.match(r'import', i):  # Если строка начинается с import
                    tmp = i.split()
                    for f in languages['python']:
                        for s in languages['python'][f]['lib']:
                            if re.match(s, tmp[1]):
                                languages['python'][f]['counter'] += 1
                                if re.match(r'as', tmp[2]):
                                    languages['python'][f]['methods'].extend(tmp[-1:])
    data = []
    for i in languages['python']:
        temp = 0
        if languages['python'][i]['counter'] > 0:
            for j in languages['python'][i]['methods']:
                temp += len(re.findall(j, string))
            for j in languages['python'][i]['lib']:
                temp += len(re.findall(j, string))
            languages['python'][i]['counter'] = temp
            data.append({"string": languages['python'][i]['lib'][0], 'counter': languages['python'][i]['counter']})

            #print(languages['python'][i])
    print(data)
    return data

framework_detector(string_2)


