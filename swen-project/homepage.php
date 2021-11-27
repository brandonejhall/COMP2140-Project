<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="index.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

    <title>Document</title>
</head>
<body>
    <?php include 'assets/php/header.php';?>
    
    <div class="body1">
        <div id="body-head">
            <h1>Placement and Career Services</h1>
            
        </div>
        <div class="form-group">
            <div id="contents">
                <h2>Career Services Form</h2>
                <form action="" id="myform" method="post">
                    <fieldset>
                        <div class="form-input">
                            <label for="name">Enter Name: <em>(Required)</em></label>
                            <input type="name" id="name" placeholder="eg. John Doe" require>
                        </div>
                        <div class="form-input">
                            <label for="id">Enter ID#: <em>(Required)</label>
                            <input type="id" id="id" placeholder="eg. 123456789" require>
                        </div>
                        <div class="form-input">
                            <label for="email">Enter Email: <em>(Required)</label>
                            <input type="email" id="email" placeholder="eg. johndoe@mymona.uwi.edu" require>
                        </div>    
                        <div class="form-input">
                            <label for="reason">Reason: <em>(Required)</label>
                            <select class="form-control" name="reason" id="reason" require>
                                <option value="a">a</option>
                                <option value="b">b</option>
                                <option value="c">c</option>
                            </select>
                        </div>      
                    </fieldset> 
                </form>                 
            </div>  
            <div class="form-button">
                <button id="form-submit">Submit</button>
            </div>               
        </div>
        
    </div>
    <?php include 'assets/php/footer.php';?>
    
</body>
</html>