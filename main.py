from vertex import Vertex
from graph import Graph
import utills

def test(file, file1):
    file_content = utills.get_file_content_list(file)
    adjecency_list = utills.get_adjecency_list(file_content)

    graph = Graph(adjecency_list)
    path = graph.bfs(Vertex(2, 0), Vertex(2, 9))
    if path != -1:
        print(len(path))
    print(path)

    utills.write_result_to_file(file1, file_content, path)


if __name__ == '__main__':
    test('input.txt', 'output.txt')
    test('input1.txt', 'output1.txt')