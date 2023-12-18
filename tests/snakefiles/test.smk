
rule all:
    input:
        "test.txt"


rule make_test:
    """test docstring"""
    output:
        "test.txt"
    shell:
        """
        (
        echo "test" > {output};
        ) &> {log}
        """

rule make_test2:
    output:
        out="test2.txt"
    log:
        "logs/make_test2.log"
    shell:
        """
        (
        echo "test2" > {output};
        ) &> {log}
        """
