def input_scores(name):
    print('{}さん。得点入力してね' .format(name))

    network = int(input('ネットワーク得点>>'))
    database = int(input('データベース得点>>'))
    security = int(input('セキュリティー得点>>'))

    scores = [network, database, security]

    return scores


def calc_average(scores):
    ave = sum(scores) / len(scores)

    return ave


def output_result(name, ave):
    print('{}さんの平均点は{}点ですよｗ' .format(name, ave))


name = input('name>>')
output_result(name, calc_average(input_scores(name)))

