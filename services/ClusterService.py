from flask import jsonify

class ClusterService():
    def __init__(self) -> None:
        pass

    def clusterPrograms(self):
        pass

    def clusterTestFunction(self, submissions: dict):
        # This is just for testing
        n = 3
        submissionIds = [list(x.keys())[0] for x in submissions]
        nElements = round(len(submissionIds)/n)

        clusters = []
        for i in range(n):
            clusters.append(submissionIds[:nElements])
            submissionIds = submissionIds[nElements:]

        return jsonify(
            clustes = clusters,
            no_cluster = len(clusters)
        )