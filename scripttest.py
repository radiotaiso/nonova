from scripttest import TestFileEnvironment

env = TestFileEnvironment('./tests')

def test_script()
    env.reset()
    result = env.run('python nonova.py -a')
    assert result.stdout.startswith('Creating new text file...')
