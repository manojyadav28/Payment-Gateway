$(document).ready(function () {
    $("#id_payment_type").change(function () {
        var payMode = this.value;
        var htmlVar = '';
        if (payMode == 'CC') {
            $("#card_number").removeClass('d-none');
            $("#card_exp_date").removeClass('d-none');
            $("#cvv").removeClass('d-none');
            // $("#upi").addClass('d-none');
            htmlVar = '<option value="" selected="">Select MOP Payment Type</option><option value="MC">Master</option><option value="VS">Visa</option><option value="RU">RuPay</option>'
            $("#id_mop_type").html(htmlVar);
        } else if (payMode == 'DC') {
            $("#card_number").removeClass('d-none');
            $("#card_exp_date").removeClass('d-none');
            $("#cvv").removeClass('d-none');
            $("#upi").addClass('d-none');
            htmlVar = '<option value="" selected="">Select MOP Payment Type</option><option value="MC">Master</option><option value="VI">Visa</option><option value="MS">Maestro</option><option value="RU">RuPay</option>'
            $("#id_mop_type").html(htmlVar);
        } else if (payMode == 'NB') {
            $("#card_number").addClass('d-none');
            $("#card_exp_date").addClass('d-none');
            $("#cvv").addClass('d-none');
            $("#upi").addClass('d-none');
            htmlVar = '<option value="" selected="">Select MOP Payment Type</option><option value="1001">Yes Bank</option><option value="1003">Industrial Development Bank Of India</option><option value="1004">HDFC Bank</option><option value="1009">Bank of India</option><option value="1012">Kotak bank</option><option value="1013">Icici Bank</option><option value="1026">Deutsche Bank</option><option value="1027">FEDERAL BANK</option><option value="1030">State Bank Of India</option><option value="1032">Karnataka Bank Ltd</option><option value="1040">Development Credit Bank</option><option value="1041">Jammu And Kashmir Bank</option><option value="1045">South Indian Bank</option><option value="1048">KarurVysya Bank</option><option value="1049">Indian Overseas Bank</option><option value="1054">IndusInd Bank</option><option value="1055">Canara Bank</option><option value="1060">City Union Bank</option><option value="1063">Central Bank Of India</option><option value="1064">Bank Of Maharashtra</option><option value="1065">Tamilnad Mercantile Bank</option><option value="1069">INDIAN BANK</option><option value="1095">Lakshmi Vilas Bank NetBanking</option><option value="1103">UCO Bank</option><option value="1104">COSMOS Bank</option><option value="1107">DHANALAXMI BANK</option><option value="1113">SHAMRAO VITHAL COOPERATIVE BANK</option>v<option value="1120">IDFC BANK</option><option value="1129">Punjab National Bank</option>'
            $("#id_mop_type").html(htmlVar);
        } else if (payMode == 'WL') {
            $("#card_number").addClass('d-none');
            $("#card_exp_date").addClass('d-none');
            $("#cvv").addClass('d-none');
            $("#upi").removeClass('d-none');
            htmlVar = '<option value="" selected="">Select MOP Payment Type</option><option value="101">Paytm</option><option value="1024">Amazon Pay</option><option value="102">Mobikwik</option><option value="103">Airtel Money</option><option value="106">RELIANCE JIO</option><option value="107">OLA MONEY</option><option value="113">FREECHARGE</option><option value="115">PHONEPE</option><option value="112">PayZapp</option>'
            $("#id_mop_type").html(htmlVar);
        }else if (payMode == 'UP') {
            $("#card_number").addClass('d-none');
            $("#card_exp_date").addClass('d-none');
            $("#cvv").addClass('d-none');
            $("#upi").removeClass('d-none');
            htmlVar = '<option value="" selected="">Select MOP Payment Type</option><option value="UP">UPI</option>'
            $("#id_mop_type").html(htmlVar);

        }

    });
});