from sampleapi import app
import unittest

class APITest(unittest.TestCase):

# Test the index route ('/')
    #Check for 200 response
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #Check if the response is json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')

    #Check if data contains the correct message
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertTrue(b'api data can be accessed at /batch_jobs' in response.data)

#Test for the batch route (/batch_jobs)
    #Check for 200 response
    def test_batch_jobs(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    #Check if the response is json
    def test_batch_content(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs')
        self.assertEqual(response.content_type, 'application/json; charset=utf-8')

    #Check if data not empty
    def test_batch_data(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs')
        self.assertTrue(b'link' in response.data)

#Test endpoint filtering
    # Check for 200 response
    def test_batch_jobs_filter_all(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_before]=2018-03-04T23:52:49+00:00'
                              '&filter[submitted_after]=2018-03-04T22:33:37+00:002'
                              '&filter[min_nodes]=0&filter[max_nodes]=1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if the response is json
    def test_batch_content_filter_all(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_before]=2018-03-04T23:52:49+00:00'
                              '&filter[submitted_after]=2018-03-04T22:33:37+00:002'
                              '&filter[min_nodes]=0&filter[max_nodes]=1')
        self.assertEqual(response.content_type, 'application/json; charset=utf-8')

    # Check if data contains the correct message
    def test_batch_data_filter_all(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_before]=2018-03-04T23:52:49+00:00'
                              '&filter[submitted_after]=2018-03-04T22:33:37+00:002'
                              '&filter[min_nodes]=0&filter[max_nodes]=1')
        self.assertTrue(b'"nodes_used": 1' in response.data)

# Check for 200 response
    def test_batch_jobs_filter_before(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_before]=2018-02-28T00:00:01+00:00')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if the response is json
    def test_batch_content_filter_before(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_before]=2018-02-28T00:00:01+00:00')
        self.assertEqual(response.content_type, 'application/json; charset=utf-8')

    # Check if data contains the correct message
    def test_batch_data_filter_before(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_before]=2018-02-28T00:00:01+00:00')
        self.assertTrue(b'"nodes_used": 2054' in response.data)

# Check for 200 response
    def test_batch_jobs_filter_after(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_after]=2018-03-04T23:52:49+00:00')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if the response is json
    def test_batch_content_filter_after(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_after]=2018-03-04T23:52:49+00:00')
        self.assertEqual(response.content_type, 'application/json; charset=utf-8')

    # Check if data contains the correct message
    def test_batch_data_filter_after(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[submitted_after]=2018-03-04T23:52:49+00:00')
        self.assertTrue(b'"nodes_used": 9623' in response.data)

# Check for 200 response
    def test_batch_jobs_filter_minNodes(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[min_nodes]=19936')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if the response is json
    def test_batch_content_filter_minNodes(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[min_nodes]=19936')
        self.assertEqual(response.content_type, 'application/json; charset=utf-8')

    # Check if data contains the correct message
    def test_batch_data_filter_minNodes(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[min_nodes]=19936')
        self.assertTrue(b'"batch_number": 166' in response.data)

# Check for 200 response
    def test_batch_jobs_filter_maxNodes(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[max_nodes]=1')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if the response is json
    def test_batch_content_filter_maxNodes(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[max_nodes]=1')
        self.assertEqual(response.content_type, 'application/json; charset=utf-8')

    # Check if data contains the correct message
    def test_batch_data_filter_maxNodes(self):
        tester = app.test_client(self)
        response = tester.get('/batch_jobs?filter[max_nodes]=1')
        self.assertTrue(b'"batch_number": 997' in response.data)

if __name__ == '__main__':
    unittest.main()

