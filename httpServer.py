'''
TODO: 
    1. Put ParseJSON in another file and import it into this file
    2. Rest of instructions on list
    3. Have a conversation/reading on API orchestration
'''

from http.server import HTTPServer, BaseHTTPRequestHandler
import json



class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    # Load the JSON data into a dictionary
    with open('dictionary.json', 'r') as json_file:
        data_dict = json.load(json_file)
    
    def do_GET(self):
        key = self.path.split('/')[-1]
        if key in self.data_dict:
            self.send_response(200)  # 200 OK
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {key: self.data_dict[key]}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)  # 404 Not Found
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'error': 'Key not found'}
            self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length).decode('utf-8')
        data_dict = json.loads(data)  # Convert JSON data to dictionary
        
        #get the key from the URL
        key = self.path.split('/')[-1]
        value=data_dict.get(key,None)
        self.data_dict[key]=value

        #update the key
        self.data_dict[key]=value

        # Send response
        self.send_response(200)  # 200 OK
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'message': 'Resource updated or created'}
        self.wfile.write(json.dumps(response).encode())

        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):
        key = self.path.split('/')[-1]

        if key in self.data_dict:
            del self.data_dict[key]
            #not going to do it here, but we could update the JSON file loaded in here
            '''
            with open('dictionary.json','w') as json_file:
                json.dump(self.data_dict,json_file,indent=4)
            '''
            #write response saying it's ok
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            response = {'message': f'Key "{key}" deleted'}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_reponse(404)#not found - i.e. not in file
            self.send_header('Content-type','application/json')
            self.end_headers()
            response = {'message': f'Key "{key}" deleted'}
            self.wfile.write(json.dumps(response).encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('Server running at http://localhost:8000')
    httpd.serve_forever()