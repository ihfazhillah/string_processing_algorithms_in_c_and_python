# string_processing_algorithms_in_c_and_python
This repository gathers implementation of algorithms related to string processing.

* Main contributors

  [@JoaoGFarias](https://github.com/JoaoGFarias)
  
  [@rmf4](https://github.com/rmf4)
  
* Algorithms implemented so far

By following those steps, you'll install the application development environment

1. Clone Git repository:
  ```bash
  $ git clone git@github.com:JoaoGFarias/string_processing_algorithms_in_c_and_python.git
  ```
2. Create a [`virtualenv`](https://virtualenv.pypa.io/en/latest/index.html) to host the application:
  You may need `sudo` to install `virtualenv` globally
  ```bash
  # install virtualenv tool manager via pip
  $ [sudo] pip install virtualenv
  # create a new virtualenv folder called venv
  $ virtualenv venv
  # activate your virtualenv!
  $ source venv/bin/activate
  ```
3. Install application dependencies via pip:
  **/!\ Be sure to have your virtualenv activated /!\\**
  This is stipulated by `(venv)` in front of your terminal prompt.

  ```bash
  (venv) $ pip install -r requirements.txt
  ```

4. Walk through the folders and test if everything runs well:
  ```bash
  (venv) $ python kmp.py
  (venv) $ python boyermoore.py
  ```
5. You can modify the input text and the input pattern as well in the source code
  
