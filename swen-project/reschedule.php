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
    <?php include 'assets/php/header.php'?>
    <div class="body1">
        <div id="body-head">
            <h1>Placement and Career Services</h1>
            
        </div>

        <div class="form-group">
            <div id="contents">
                <h2>Career Services Reschedule Form</h2>
                <form action="" id="myform" method="post">
                    <fieldset>
                        <div class="form-input">
                            <label for="reference">Reference#: <em>(Required)</em></label>
                            <input type="refernce" id="reference" placeholder="eg.84521778" require>
                        </div>
                        <div class="form-input">
                            <label for="id">Enter ID#: <em>(Required)</label>
                            <input type="id" id="id" placeholder="eg. 123456789" require>
                        </div>
                        <div class="form-input">
                            <label for="new-date">New Date <em>(Required)</label>
                            <input type="text" id="new-date" placeholder="" require>
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
                    <div class="reschedule-form-button">
                        <button id="reschedule-submit">Submit</button>
                    </div>   
                </form>   
            </div>
              
        </div>
        
    </div>
    <?php include 'assets/php/footer.php';?>
</body>
</html>